import streamlit as st
import git
from git_utils import (
    commit_types,
    create_commit_message,
    execute_commit,
    execute_merge,
    execute_checkout,
    execute_create_branch,
    execute_pull,
    execute_push,
    get_git_graph_data,
    repo_path
)

try:
    from graphviz import Digraph
    GRAPHVIZ_AVAILABLE = True
except ImportError:
    GRAPHVIZ_AVAILABLE = False

def render_git_graph(commit_data, refs):
    """graphviz를 사용하여 Git 그래프를 렌더링"""
    if not GRAPHVIZ_AVAILABLE:
        st.warning("Graphviz is not installed. Please run `pip install graphviz` to see the visual git graph.")
        return

    # Create a mapping from sha to a list of refs
    ref_map = {}
    for ref_name, ref_info in refs.items():
        sha = ref_info['sha']
        if sha not in ref_map:
            ref_map[sha] = []
        ref_map[sha].append({'name': ref_name, 'type': ref_info['type']})

    dot = Digraph()
    dot.attr('graph', rankdir='TB', splines='ortho')
    dot.attr('node', shape='box', style='rounded,filled', fontname='Arial', fontsize='12')
    dot.attr('edge', arrowhead='none')

    commit_nodes = set()
    for commit in commit_data:
        sha = commit['sha']
        short_sha = commit['short_sha']
        message = commit['message']
        author = commit['author']
        
        if sha in commit_nodes:
            continue
        commit_nodes.add(sha)

        # Create a cluster for commit and its refs
        with dot.subgraph(name=f'cluster_{sha}') as c:
            c.attr(color='invis')
            
            # Commit Node
            commit_label = f'<{short_sha}<br/><b>{message}</b><br/><font point-size="10" color="gray">{author}</font>>'
            c.node(sha, label=commit_label, shape='box', style='rounded', fillcolor='lightcyan')

            # Refs Node
            if sha in ref_map:
                ref_label_parts = []
                for ref in ref_map[sha]:
                    color = {
                        'branch': 'lightgreen',
                        'remote': 'orange',
                        'tag': 'lightblue'
                    }.get(ref['type'], 'lightgrey')
                    ref_label_parts.append(f'<font color="black" bgcolor="{color}">{ref["name"]}</font>')
                ref_label = '<' + '&nbsp;'.join(ref_label_parts) + '>'
                
                ref_node_id = f"ref_{sha}"
                c.node(ref_node_id, label=ref_label, shape='box', style='rounded,filled', fillcolor='whitesmoke')
                c.edge(ref_node_id, sha, style='invis', arrowhead='none', minlen='1')

        # Edges to parents
        for parent_sha in commit['parents']:
            if parent_sha in [c['sha'] for c in commit_data]:
                dot.edge(parent_sha, sha)

    st.graphviz_chart(dot, use_container_width=True)


def main():
    st.set_page_config(page_title="Git Tool", layout="wide")

    # Display session messages
    if 'success_message' in st.session_state and st.session_state.success_message:
        st.success(st.session_state.success_message)
        st.session_state.success_message = None
    if 'error_message' in st.session_state and st.session_state.error_message:
        st.error(st.session_state.error_message)
        st.session_state.error_message = None

    # Title and Refresh Button
    col1, col2, _ = st.columns([0.5, 0.1, 0.4])
    with col1:
        st.title("Git Commit/Merge Formatter")
    with col2:
        if st.button("🔄", help="Refresh the app state"):
            st.rerun()

    try:
        repo = git.Repo(repo_path)
        branches = [b.name for b in repo.branches]
        current_branch = repo.active_branch.name
    except git.InvalidGitRepositoryError:
        st.error("This is not a Git repository. Please run this tool in a valid Git repository.")
        return
    except Exception as e:
        st.error(f"An error occurred while reading the repository: {e}")
        return

    # Sidebar
    st.sidebar.header("Actions")
    action_type = st.sidebar.selectbox(
        "Select Action",
        ["Commit", "Merge", "Create Branch", "Pull", "Push", "Checkout Branch"]
    )
    st.sidebar.markdown("---")
    st.sidebar.header("Current Status")
    st.sidebar.info(f"**Current Branch:** `{current_branch}`")
    
    # Git Graph
    st.markdown("## Git Graph")
    commit_data, refs = get_git_graph_data()
    if commit_data:
        render_git_graph(commit_data, refs)
    else:
        st.info("No commits in the repository yet.")

    # Main action handling
    st.markdown("---")
    st.header(f"Action: {action_type}")

    if action_type == "Commit":
        st.subheader("Create a new commit")
        commit_type = st.selectbox("Commit Type", commit_types)
        commit_title = st.text_input("Commit Title")
        commit_description = st.text_area("Commit Description", height=200)
        
        if st.button("Execute Commit"):
            if not commit_title:
                st.warning("Commit title is required.")
            else:
                commit_message = create_commit_message(commit_type, commit_title, commit_description)
                error = execute_commit(commit_message)
                if error:
                    st.session_state.error_message = error
                else:
                    st.session_state.success_message = "Commit successful!"
                st.rerun()

    elif action_type == "Merge":
        st.subheader("Merge branches")
        target_branch = st.selectbox("Target Branch (into which you merge)", branches, index=branches.index(current_branch))
        source_branch = st.selectbox("Source Branch (which you merge)", [b for b in branches if b != target_branch])

        if st.button("Execute Merge"):
            error = execute_merge(source_branch, target_branch)
            if error:
                st.session_state.error_message = error
            else:
                st.session_state.success_message = f"Successfully merged `{source_branch}` into `{target_branch}`!"
            st.rerun()

    elif action_type == "Create Branch":
        st.subheader("Create a new branch")
        base_branch = st.selectbox("Base Branch", branches, index=branches.index(current_branch))
        new_branch_name = st.text_input("New Branch Name")

        if st.button("Create Branch"):
            if not new_branch_name:
                st.warning("New branch name is required.")
            else:
                error = execute_create_branch(new_branch_name, base_branch)
                if error:
                    st.session_state.error_message = error
                else:
                    st.session_state.success_message = f"Branch `{new_branch_name}` created successfully from `{base_branch}`!"
                st.rerun()

    elif action_type == "Pull":
        st.subheader("Pull changes from remote")
        pull_branch = st.selectbox("Branch to pull", branches, index=branches.index(current_branch))
        
        if st.button("Execute Pull"):
            with st.spinner(f"Pulling changes for `{pull_branch}`..."):
                error = execute_pull(pull_branch)
                if error:
                    st.session_state.error_message = error
                else:
                    st.session_state.success_message = f"Successfully pulled changes for `{pull_branch}`!"
                st.rerun()

    elif action_type == "Push":
        st.subheader("Push changes to remote")
        push_branch = st.selectbox("Branch to push", branches, index=branches.index(current_branch))

        if st.button("Execute Push"):
            with st.spinner(f"Pushing changes for `{push_branch}`..."):
                error = execute_push(push_branch)
                if error:
                    st.session_state.error_message = error
                else:
                    st.session_state.success_message = f"Successfully pushed changes for `{push_branch}`!"
                st.rerun()

    elif action_type == "Checkout Branch":
        st.subheader("Switch to a different branch")
        checkout_branch = st.selectbox("Select Branch to Checkout", [b for b in branches if b != current_branch])

        if st.button("Checkout"):
            error = execute_checkout(checkout_branch)
            if error:
                st.session_state.error_message = error
            else:
                st.session_state.success_message = f"Switched to branch `{checkout_branch}`."
            st.rerun()

if __name__ == '__main__':
    main() 