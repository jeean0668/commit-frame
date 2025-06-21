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

def main():
    st.set_page_config(page_title="Git Tool", layout="wide")

    st.title("Git Commit/Merge Formatter")

    try:
        repo = git.Repo(repo_path)
        branches = [branch.name for branch in repo.branches]
        current_branch = repo.active_branch.name
    except git.InvalidGitRepositoryError:
        st.error("This is not a Git repository. Please run this tool in a valid Git repository.")
        return
    except Exception as e:
        st.error(f"An error occurred while reading the repository: {e}")
        return

    # --- 사이드바 ---
    st.sidebar.header("Actions")
    action_type = st.sidebar.selectbox(
        "Select Action",
        ["Commit", "Merge", "Create Branch", "Pull", "Push", "Checkout Branch"]
    )

    st.sidebar.markdown("---")
    st.sidebar.header("Current Status")
    st.sidebar.info(f"**Current Branch:** `{current_branch}`")
    
    # --- Git Graph ---
    st.markdown("## Git Graph")
    graph_data = get_git_graph_data()
    if graph_data:
        for commit in graph_data:
            branch_tags = " ".join([f"`{branch}`" for branch in commit['branches']])
            st.markdown(
                f"- **{commit['hash']}**: {commit['message']} (*{commit['author']}*, {commit['date']}) {branch_tags}"
            )
    else:
        st.info("No commits in the repository yet.")


    # --- 메인 액션 핸들링 ---
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
                    st.error(error)
                else:
                    st.success("Commit successful!")
                    st.experimental_rerun()

    elif action_type == "Merge":
        st.subheader("Merge branches")
        target_branch = st.selectbox("Target Branch (into which you merge)", branches, index=branches.index(current_branch))
        source_branch = st.selectbox("Source Branch (which you merge)", [b for b in branches if b != target_branch])

        if st.button("Execute Merge"):
            error = execute_merge(source_branch, target_branch)
            if error:
                st.error(error)
            else:
                st.success(f"Successfully merged `{source_branch}` into `{target_branch}`!")
                st.experimental_rerun()

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
                    st.error(error)
                else:
                    st.success(f"Branch `{new_branch_name}` created successfully from `{base_branch}`!")
                    st.experimental_rerun()

    elif action_type == "Pull":
        st.subheader("Pull changes from remote")
        pull_branch = st.selectbox("Branch to pull", branches, index=branches.index(current_branch))
        
        if st.button("Execute Pull"):
            with st.spinner(f"Pulling changes for `{pull_branch}`..."):
                error = execute_pull(pull_branch)
                if error:
                    st.error(error)
                else:
                    st.success(f"Successfully pulled changes for `{pull_branch}`!")
                    st.experimental_rerun()

    elif action_type == "Push":
        st.subheader("Push changes to remote")
        push_branch = st.selectbox("Branch to push", branches, index=branches.index(current_branch))

        if st.button("Execute Push"):
            with st.spinner(f"Pushing changes for `{push_branch}`..."):
                error = execute_push(push_branch)
                if error:
                    st.error(error)
                else:
                    st.success(f"Successfully pushed changes for `{push_branch}`!")
                    st.experimental_rerun()

    elif action_type == "Checkout Branch":
        st.subheader("Switch to a different branch")
        checkout_branch = st.selectbox("Select Branch to Checkout", [b for b in branches if b != current_branch])

        if st.button("Checkout"):
            error = execute_checkout(checkout_branch)
            if error:
                st.error(error)
            else:
                st.success(f"Switched to branch `{checkout_branch}`.")
                st.experimental_rerun()

if __name__ == '__main__':
    main() 