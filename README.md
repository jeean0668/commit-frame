# Git Commit Tool

Git 커밋과 머지를 웹 인터페이스를 통해 쉽게 수행할 수 있는 도구입니다.

## 기능

- 웹 인터페이스를 통한 Git 커밋 생성
- 커밋 메시지 템플릿 지원
- 브랜치 간 머지 기능
- 실시간 커밋/머지 상태 확인

## 환경 요구사항

- Python 3.6 이상
- Git
- pip (Python 패키지 관리자)

## 설치 방법

1. 저장소 클론
```bash
git clone [repository-url]
cd commit-frame
```

2. 필요한 Python 패키지 설치
```bash
pip install flask gitpython
```

## 사용 방법

1. 프로젝트 설정
   - Git으로 관리하고 있는 프로젝트 디렉토리로 이동
   - `templates` 폴더와 `git_commit_tool.py` 파일을 프로젝트 루트 디렉토리에 복사

2. 도구 실행
   ```bash
   python git_commit_tool.py
   ```

3. 웹 브라우저에서 다음 주소로 접속
   ```
   http://localhost:5000
   ```

4. 커밋 메시지 작성
   - 커밋 타입 선택 (feat, fix, docs 등)
   - 커밋 제목 입력
   - 커밋 설명 입력
   - 'Execute' 버튼 클릭

5. 브랜치 머지하기 (선택사항)
   - 소스 브랜치 선택
   - 타겟 브랜치 선택
   - 'Merge' 버튼 클릭

## 주의사항

- 이 도구는 Git 저장소가 초기화된 디렉토리에서 실행해야 합니다.
- 실행 전에 Git 사용자 정보가 올바르게 설정되어 있어야 합니다.
- 머지 작업 시 충돌이 발생할 수 있으니 주의하세요.

## 문제 해결

문제가 발생하면 다음을 확인하세요:
1. Git이 올바르게 설치되어 있는지
2. Python과 필요한 패키지가 설치되어 있는지
3. 현재 디렉토리가 Git 저장소인지
4. Git 사용자 정보가 올바르게 설정되어 있는지
