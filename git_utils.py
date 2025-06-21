import os
import git

# 커밋 타입 옵션
commit_types = ['feat', 'fix', 'docs', 'style', 'refactor', 'test', 'chore', 'build']

# Git 리포지토리 경로
repo_path = os.getcwd()  # 현재 작업 디렉토리로 설정, 필요에 따라 수정

def create_commit_message(commit_type, commit_title, commit_description):
    """커밋 메시지를 정형화하여 반환"""
    commit_message = f"<{commit_type}>: {commit_title}\n<title>: {commit_title}\n<body>: {commit_description}"
    return commit_message

def execute_commit(commit_message):
    """Git 리포지토리에서 커밋을 실행"""
    try:
        repo = git.Repo(repo_path)
        repo.git.add(A=True)  # 모든 변경사항 스테이징
        repo.index.commit(commit_message)  # 커밋 메시지 적용
    except git.exc.GitCommandError as e:
        error_message = e.stderr
        if isinstance(error_message, bytes):
            error_message = error_message.decode('utf-8')
            
        if "nothing to commit" in error_message.lower():
            return "Nothing to commit. No changes detected."
        elif "not a git repository" in error_message.lower():
            return "Not a Git repository. Please check if the path is correct."
        else:
            return f"Error during commit: {error_message}"
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"
    return None

def execute_merge(source_branch, target_branch):
    """Git 리포지토리에서 머지 작업을 실행"""
    try:
        repo = git.Repo(repo_path)
        origin = repo.remotes.origin
        origin.fetch()  # 원격 저장소 업데이트
        repo.git.checkout(target_branch)  # 대상 브랜치로 체크아웃
        repo.git.merge(source_branch)  # 소스 브랜치를 대상 브랜치에 머지
    except git.exc.GitCommandError as e:
        error_message = e.stderr
        if isinstance(error_message, bytes):
            error_message = error_message.decode('utf-8')
            
        if "conflict" in error_message.lower():
            return "Merge conflict detected. Please resolve conflicts."
        elif "not a git repository" in error_message.lower():
            return "Not a Git repository. Please check if the path is correct."
        elif "couldn't find remote ref" in error_message.lower():
            return "Remote branch not found."
        else:
            return f"Error during merge: {error_message}"
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"
    return None

def execute_checkout(branch):
    """Git 리포지토리에서 브랜치 체크아웃을 실행"""
    try:
        repo = git.Repo(repo_path)
        repo.git.checkout(branch)
    except git.exc.GitCommandError as e:
        error_message = e.stderr
        if isinstance(error_message, bytes):
            error_message = error_message.decode('utf-8')
            
        if "did not match any file" in error_message.lower():
            return f"Branch '{branch}' not found."
        elif "not a git repository" in error_message.lower():
            return "Not a Git repository. Please check if the path is correct."
        elif "local changes would be overwritten" in error_message.lower():
            return "Local changes would be overwritten. Please commit or stash your changes."
        else:
            return f"Error during checkout: {error_message}"
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"
    return None

def execute_create_branch(new_branch_name, base_branch):
    """새로운 브랜치를 생성하고 체크아웃"""
    try:
        repo = git.Repo(repo_path)
        # 기본 브랜치로 체크아웃
        repo.git.checkout(base_branch)
        # 새 브랜치 생성 및 체크아웃
        repo.git.checkout('-b', new_branch_name)
    except git.exc.GitCommandError as e:
        error_message = e.stderr
        if isinstance(error_message, bytes):
            error_message = error_message.decode('utf-8')
            
        if "already exists" in error_message.lower():
            return f"Branch '{new_branch_name}' already exists."
        elif "not a git repository" in error_message.lower():
            return "Not a Git repository. Please check if the path is correct."
        elif "did not match any file" in error_message.lower():
            return f"Base branch '{base_branch}' not found."
        else:
            return f"Error during branch creation: {error_message}"
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"
    return None

def execute_pull(branch):
    """Git 리포지토리에서 pull 작업을 실행"""
    try:
        repo = git.Repo(repo_path)
        origin = repo.remotes.origin
        origin.fetch()  # 원격 저장소 업데이트
        repo.git.checkout(branch)  # 해당 브랜치로 체크아웃
        repo.git.pull('origin', branch)  # 원격 저장소에서 pull
    except git.exc.GitCommandError as e:
        error_message = e.stderr
        if isinstance(error_message, bytes):
            error_message = error_message.decode('utf-8')
        
        if "conflict" in error_message.lower():
            return "Conflict detected. Local changes conflict with remote changes."
        elif "not a git repository" in error_message.lower():
            return "Not a Git repository. Please check if the path is correct."
        elif "couldn't find remote ref" in error_message.lower():
            return f"Remote branch '{branch}' not found."
        elif "authentication failed" in error_message.lower():
            return "Authentication failed. Please check your GitHub credentials."
        elif "permission denied" in error_message.lower():
            return "Permission denied. Please check your repository access rights."
        elif "already up to date" in error_message.lower():
            return "Already up to date. No updates available."
        else:
            return f"Error during pull: {error_message}"
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"
    return None

def execute_push(branch):
    """Git 리포지토리에서 push 작업을 실행"""
    try:
        repo = git.Repo(repo_path)
        origin = repo.remotes.origin
        repo.git.checkout(branch)  # 해당 브랜치로 체크아웃
        repo.git.push('origin', branch)  # 원격 저장소로 push
    except git.exc.GitCommandError as e:
        error_message = e.stderr
        if isinstance(error_message, bytes):
            error_message = error_message.decode('utf-8')
        
        if "not a git repository" in error_message.lower():
            return "Not a Git repository. Please check if the path is correct."
        elif "authentication failed" in error_message.lower():
            return "Authentication failed. Please check your GitHub credentials."
        elif "permission denied" in error_message.lower():
            return "Permission denied. Please check your repository access rights."
        elif "rejected" in error_message.lower():
            return "Push rejected. Please pull latest changes first."
        else:
            return f"Error during push: {error_message}"
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"
    return None

def get_git_graph_data():
    """Git 그래프에 필요한 커밋과 참조 데이터를 가져오는 함수"""
    try:
        repo = git.Repo(repo_path)
        
        # 모든 커밋 가져오기
        commits = list(repo.iter_commits('--all'))
        
        commit_data = []
        for commit in commits:
            commit_data.append({
                'sha': commit.hexsha,
                'short_sha': commit.hexsha[:7],
                'message': commit.message.split('\n')[0],
                'author': commit.author.name,
                'date': commit.committed_datetime.strftime('%Y-%m-%d %H:%M'),
                'parents': [p.hexsha for p in commit.parents]
            })
            
        # 모든 참조(브랜치, 원격 브랜치, 태그) 가져오기
        refs = {}
        # 로컬 브랜치
        for branch in repo.branches:
            refs[branch.name] = {'type': 'branch', 'sha': branch.commit.hexsha}
        
        # 원격 브랜치
        for remote in repo.remotes:
            for ref in remote.refs:
                if 'HEAD' in ref.name:
                    continue
                refs[ref.name] = {'type': 'remote', 'sha': ref.commit.hexsha}
        
        # 태그
        for tag in repo.tags:
            refs[tag.name] = {'type': 'tag', 'sha': tag.commit.hexsha}

        return commit_data, refs
    except Exception as e:
        print(f"Failed to get git data: {e}")
        return [], {} 