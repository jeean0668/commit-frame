import os
from flask import Flask, render_template, request, redirect, url_for, jsonify
import git
import threading
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

# Flask 앱 설정
app = Flask(__name__)

# 커밋 타입 옵션
# commit_types = ['feat', 'fix', 'docs', 'style', 'refactor', 'test', 'chore', 'build']

# Git 리포지토리 경로
# repo_path = os.getcwd()  # 현재 작업 디렉토리로 설정, 필요에 따라 수정

# def create_commit_message(commit_type, commit_title, commit_description):
#     """커밋 메시지를 정형화하여 반환"""
#     commit_message = f"<{commit_type}>: {commit_title}\n<title>: {commit_title}\n<body>: {commit_description}"
#     return commit_message

# def execute_commit(commit_message):
#     """Git 리포지토리에서 커밋을 실행"""
#     try:
#         repo = git.Repo(repo_path)
#         repo.git.add(A=True)  # 모든 변경사항 스테이징
#         repo.index.commit(commit_message)  # 커밋 메시지 적용
#     except git.exc.GitCommandError as e:
#         error_message = e.stderr
#         if isinstance(error_message, bytes):
#             error_message = error_message.decode('utf-8')
            
#         if "nothing to commit" in error_message.lower():
#             return "Nothing to commit. No changes detected."
#         elif "not a git repository" in error_message.lower():
#             return "Not a Git repository. Please check if the path is correct."
#         else:
#             return f"Error during commit: {error_message}"
#     except Exception as e:
#         return f"An unexpected error occurred: {str(e)}"
#     return None

# def execute_merge(source_branch, target_branch):
#     """Git 리포지토리에서 머지 작업을 실행"""
#     try:
#         repo = git.Repo(repo_path)
#         origin = repo.remotes.origin
#         origin.fetch()  # 원격 저장소 업데이트
#         repo.git.checkout(target_branch)  # 대상 브랜치로 체크아웃
#         repo.git.merge(source_branch)  # 소스 브랜치를 대상 브랜치에 머지
#     except git.exc.GitCommandError as e:
#         error_message = e.stderr
#         if isinstance(error_message, bytes):
#             error_message = error_message.decode('utf-8')
            
#         if "conflict" in error_message.lower():
#             return "Merge conflict detected. Please resolve conflicts."
#         elif "not a git repository" in error_message.lower():
#             return "Not a Git repository. Please check if the path is correct."
#         elif "couldn't find remote ref" in error_message.lower():
#             return "Remote branch not found."
#         else:
#             return f"Error during merge: {error_message}"
#     except Exception as e:
#         return f"An unexpected error occurred: {str(e)}"
#     return None

# def execute_checkout(branch):
#     """Git 리포지토리에서 브랜치 체크아웃을 실행"""
#     try:
#         repo = git.Repo(repo_path)
#         repo.git.checkout(branch)
#     except git.exc.GitCommandError as e:
#         error_message = e.stderr
#         if isinstance(error_message, bytes):
#             error_message = error_message.decode('utf-8')
            
#         if "did not match any file" in error_message.lower():
#             return f"Branch '{branch}' not found."
#         elif "not a git repository" in error_message.lower():
#             return "Not a Git repository. Please check if the path is correct."
#         elif "local changes would be overwritten" in error_message.lower():
#             return "Local changes would be overwritten. Please commit or stash your changes."
#         else:
#             return f"Error during checkout: {error_message}"
#     except Exception as e:
#         return f"An unexpected error occurred: {str(e)}"
#     return None

# def execute_create_branch(new_branch_name, base_branch):
#     """새로운 브랜치를 생성하고 체크아웃"""
#     try:
#         repo = git.Repo(repo_path)
#         # 기본 브랜치로 체크아웃
#         repo.git.checkout(base_branch)
#         # 새 브랜치 생성 및 체크아웃
#         repo.git.checkout('-b', new_branch_name)
#     except git.exc.GitCommandError as e:
#         error_message = e.stderr
#         if isinstance(error_message, bytes):
#             error_message = error_message.decode('utf-8')
            
#         if "already exists" in error_message.lower():
#             return f"Branch '{new_branch_name}' already exists."
#         elif "not a git repository" in error_message.lower():
#             return "Not a Git repository. Please check if the path is correct."
#         elif "did not match any file" in error_message.lower():
#             return f"Base branch '{base_branch}' not found."
#         else:
#             return f"Error during branch creation: {error_message}"
#     except Exception as e:
#         return f"An unexpected error occurred: {str(e)}"
#     return None

# def execute_pull(branch):
#     """Git 리포지토리에서 pull 작업을 실행"""
#     try:
#         repo = git.Repo(repo_path)
#         origin = repo.remotes.origin
#         origin.fetch()  # 원격 저장소 업데이트
#         repo.git.checkout(branch)  # 해당 브랜치로 체크아웃
#         repo.git.pull('origin', branch)  # 원격 저장소에서 pull
#     except git.exc.GitCommandError as e:
#         error_message = e.stderr
#         if isinstance(error_message, bytes):
#             error_message = error_message.decode('utf-8')
        
#         if "conflict" in error_message.lower():
#             return "Conflict detected. Local changes conflict with remote changes."
#         elif "not a git repository" in error_message.lower():
#             return "Not a Git repository. Please check if the path is correct."
#         elif "couldn't find remote ref" in error_message.lower():
#             return f"Remote branch '{branch}' not found."
#         elif "authentication failed" in error_message.lower():
#             return "Authentication failed. Please check your GitHub credentials."
#         elif "permission denied" in error_message.lower():
#             return "Permission denied. Please check your repository access rights."
#         elif "already up to date" in error_message.lower():
#             return "Already up to date. No updates available."
#         else:
#             return f"Error during pull: {error_message}"
#     except Exception as e:
#         return f"An unexpected error occurred: {str(e)}"
#     return None

# def execute_push(branch):
#     """Git 리포지토리에서 push 작업을 실행"""
#     try:
#         repo = git.Repo(repo_path)
#         origin = repo.remotes.origin
#         repo.git.checkout(branch)  # 해당 브랜치로 체크아웃
#         repo.git.push('origin', branch)  # 원격 저장소로 push
#     except git.exc.GitCommandError as e:
#         error_message = e.stderr
#         if isinstance(error_message, bytes):
#             error_message = error_message.decode('utf-8')
        
#         if "not a git repository" in error_message.lower():
#             return "Not a Git repository. Please check if the path is correct."
#         elif "authentication failed" in error_message.lower():
#             return "Authentication failed. Please check your GitHub credentials."
#         elif "permission denied" in error_message.lower():
#             return "Permission denied. Please check your repository access rights."
#         elif "rejected" in error_message.lower():
#             return "Push rejected. Please pull latest changes first."
#         else:
#             return f"Error during push: {error_message}"
#     except Exception as e:
#         return f"An unexpected error occurred: {str(e)}"
#     return None

# def get_git_graph_data():
#     """Git 그래프 데이터를 가져오는 함수"""
#     try:
#         repo = git.Repo(repo_path)
#         commits = list(repo.iter_commits())
#         graph_data = []
        
#         for commit in commits:
#             graph_data.append({
#                 'hash': commit.hexsha[:7],
#                 'message': commit.message.split('\n')[0],
#                 'author': commit.author.name,
#                 'date': commit.committed_datetime.strftime('%Y-%m-%d %H:%M'),
#                 'branches': [b.name for b in repo.branches if b.commit.hexsha == commit.hexsha]
#             })
        
#         return graph_data
#     except Exception as e:
#         return []

@app.route('/')
def index():
    """메인 페이지 (커밋 폼 제공)"""
    repo = git.Repo(repo_path)
    branches = [branch.name for branch in repo.branches]  # 모든 로컬 브랜치 목록 가져오기
    current_branch = repo.active_branch.name  # 현재 브랜치 이름 가져오기
    graph_data = get_git_graph_data()  # 그래프 데이터 가져오기
    return render_template('index.html', 
                         commit_types=commit_types, 
                         branches=branches, 
                         current_branch=current_branch,
                         graph_data=graph_data)

@app.route('/commit', methods=['POST'])
def commit():
    """폼 데이터를 받아 Git 커밋 실행"""
    action_type = request.form.get('action_type')  # commit, merge, branch 또는 pull 선택
    if action_type == 'commit':
        commit_type = request.form.get('commit_type')
        commit_title = request.form.get('commit_title')
        commit_description = request.form.get('commit_description')

        # 커밋 메시지 생성
        commit_message = create_commit_message(commit_type, commit_title, commit_description)

        # 커밋 실행
        result_error = execute_commit(commit_message)
        if result_error:
            return redirect(url_for('failure', error=result_error))
        
        return redirect(url_for('success'))

    elif action_type == 'merge':
        # 머지할 브랜치 선택
        source_branch = request.form.get('source_branch')
        target_branch = request.form.get('target_branch')

        # 머지 실행
        result_error = execute_merge(source_branch, target_branch)
        if result_error:
            return redirect(url_for('failure', error=result_error))
        
        return redirect(url_for('success'))
    
    elif action_type == 'branch':
        # 새 브랜치 생성
        new_branch_name = request.form.get('new_branch_name')
        base_branch = request.form.get('base_branch')

        # 브랜치 생성 실행
        result_error = execute_create_branch(new_branch_name, base_branch)
        if result_error:
            return redirect(url_for('failure', error=result_error))
        
        return redirect(url_for('success'))

    elif action_type == 'pull':
        # pull할 브랜치 선택
        branch = request.form.get('pull_branch')

        # pull 실행
        result_error = execute_pull(branch)
        if result_error:
            return redirect(url_for('failure', error=result_error))
        
        return redirect(url_for('success'))
    
    elif action_type == 'push':
        # push할 브랜치 선택
        branch = request.form.get('push_branch')

        # push 실행
        result_error = execute_push(branch)
        if result_error:
            return redirect(url_for('failure', error=result_error))
        
        return redirect(url_for('success'))
    
    # 지원하지 않는 액션 타입인 경우
    return redirect(url_for('failure', error='지원하지 않는 액션 타입입니다.'))

@app.route('/success')
def success():
    """커밋 또는 머지 성공 페이지"""
    return render_template('success.html')

@app.route('/failure')
def failure():
    """커밋 또는 머지 실패 페이지"""
    error_message = request.args.get('error', 'An unknown error occurred')
    return render_template('failure.html', error_message=error_message)

@app.route('/checkout', methods=['POST'])
def checkout():
    """브랜치 체크아웃을 처리하는 엔드포인트"""
    try:
        data = request.get_json()
        branch = data.get('branch')
        if not branch:
            return jsonify({'success': False, 'error': '브랜치 이름이 제공되지 않았습니다.'})
        
        result_error = execute_checkout(branch)
        if result_error:
            return jsonify({'success': False, 'error': result_error})
        
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

def run_flask_app():
    """Flask 앱 실행"""
    app.run(debug=True, use_reloader=False, port=5000)

if __name__ == '__main__':
    # Flask 서버를 별도의 스레드로 실행
    threading.Thread(target=run_flask_app).start()
