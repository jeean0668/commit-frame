import os
from flask import Flask, render_template, request, redirect, url_for, jsonify
import git
import threading

# Flask 앱 설정
app = Flask(__name__)

# 커밋 타입 옵션
commit_types = ['feat', 'fix', 'docs', 'style', 'refactor', 'test', 'chore']

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
    except Exception as e:
        return f"An error occurred during commit: {e}"
    return None  # 성공 시 None을 반환

def execute_merge(source_branch, target_branch):
    """Git 리포지토리에서 머지 작업을 실행"""
    try:
        repo = git.Repo(repo_path)
        origin = repo.remotes.origin
        origin.fetch()  # 원격 저장소 업데이트
        repo.git.checkout(target_branch)  # 대상 브랜치로 체크아웃
        repo.git.merge(source_branch)  # 소스 브랜치를 대상 브랜치에 머지
    except git.exc.GitCommandError as e:
        # GitCommandError를 캐치해서 오류 메시지를 반환
        return f"An error occurred during merge: {e.stderr.decode('utf-8')}"
    return None  # 성공 시 None을 반환

def execute_checkout(branch):
    """Git 리포지토리에서 브랜치 체크아웃을 실행"""
    try:
        repo = git.Repo(repo_path)
        repo.git.checkout(branch)
    except git.exc.GitCommandError as e:
        return f"An error occurred during checkout: {e.stderr.decode('utf-8')}"
    return None  # 성공 시 None을 반환

@app.route('/')
def index():
    """메인 페이지 (커밋 폼 제공)"""
    repo = git.Repo(repo_path)
    branches = [branch.name for branch in repo.branches]  # 모든 로컬 브랜치 목록 가져오기
    current_branch = repo.active_branch.name  # 현재 브랜치 이름 가져오기
    return render_template('index.html', commit_types=commit_types, branches=branches, current_branch=current_branch)

@app.route('/commit', methods=['POST'])
def commit():
    """폼 데이터를 받아 Git 커밋 실행"""
    action_type = request.form.get('action_type')  # commit 또는 merge 선택
    if action_type == 'commit':
        commit_type = request.form.get('commit_type')
        commit_title = request.form.get('commit_title')
        commit_description = request.form.get('commit_description')

        # 커밋 메시지 생성
        commit_message = create_commit_message(commit_type, commit_title, commit_description)

        # 커밋 실행 (다른 스레드에서 처리하여 웹 서버가 차단되지 않도록 함)
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

@app.route('/success')
def success():
    """커밋 또는 머지 성공 페이지"""
    return render_template('success.html')

@app.route('/failure')
def failure():
    """커밋 또는 머지 실패 페이지"""
    error_message = request.args.get('error', 'An unknown error occurred.')
    return render_template('failure.html', error_message=error_message)

@app.route('/checkout', methods=['POST'])
def checkout():
    """브랜치 체크아웃 요청을 처리"""
    data = request.get_json()
    branch = data.get('branch')
    
    if not branch:
        return jsonify({'success': False, 'error': '브랜치가 지정되지 않았습니다.'})
    
    result_error = execute_checkout(branch)
    if result_error:
        return jsonify({'success': False, 'error': result_error})
    
    return jsonify({'success': True})

def run_flask_app():
    """Flask 앱 실행"""
    app.run(debug=True, use_reloader=False, port=5000)

if __name__ == '__main__':
    # Flask 서버를 별도의 스레드로 실행
    threading.Thread(target=run_flask_app).start()
