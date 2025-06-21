# Git Commit/Merge Formatter

<div style="text-align: right; margin-bottom: 20px;">
  <button onclick="toggleLanguage()" style="padding: 8px 16px; background-color: #007bff; color: white; border: none; border-radius: 4px; cursor: pointer;">
    <span id="langBtn">한국어</span>
  </button>
</div>

<div id="english-content">
A powerful Git repository management tool that helps developers create standardized commit messages and manage branches efficiently. Built with Streamlit for a modern web interface, this tool streamlines your Git workflow with structured commit templates and comprehensive branch management capabilities.

## Key Features

### 📝 Standardized Commit Messages
- **Conventional Commit Format**: Follow industry standards with predefined commit types (feat, fix, docs, style, refactor, test, chore, build)
- **Structured Templates**: Automatically format commit messages with title, body, and type sections
- **Consistent History**: Maintain clean and readable Git history across your team
- **Easy Customization**: Modify commit types and templates to match your project's conventions

### 🌿 Advanced Branch Management
- **Seamless Branch Operations**: Create, checkout, and merge branches with a few clicks
- **Visual Branch Status**: Real-time display of current branch, remote status, and commit differences
- **Safe Merge Operations**: Merge branches with conflict detection and resolution guidance
- **Remote Synchronization**: Pull and push changes with clear status feedback

### 📊 Git History Visualization
- **Interactive Git Graph**: Visualize commit history with Graphviz-powered diagrams
- **Commit Details**: View comprehensive commit information including author, date, and full message body
- **Branch and Tag Display**: See all references pointing to each commit
- **Real-time Updates**: Refresh and see the latest changes instantly

### 🎯 Modern Web Interface
- **Intuitive Design**: Clean and responsive Streamlit interface
- **Sidebar Navigation**: Quick access to all Git operations
- **Real-time Status**: Live updates of repository state
- **Cross-platform**: Works on macOS, Linux, and Windows

## Requirements

- Python 3.7 or higher
- Git
- macOS/Linux/Windows support

## Installation & Execution

### 1. Copy Project Files
Copy the following files to your target Git repository:

**Required Files:**
- `streamlit_app.py` - Main Streamlit application
- `git_utils.py` - Git utility functions
- `requirements.txt` - Python dependencies

**Copy Methods:**
```bash
# Method 1: Copy files directly
cp streamlit_app.py /path/to/your/git/repository/
cp git_utils.py /path/to/your/git/repository/
cp requirements.txt /path/to/your/git/repository/

# Method 2: Copy entire project and extract needed files
cp -r commit-frame /path/to/your/git/repository/
cd /path/to/your/git/repository/commit-frame
# Move required files to parent directory
```

### 2. Clone Repository (if working from original repo)
```bash
git clone [repository-url]
cd commit-frame
```

### 3. Create and Activate Virtual Environment

**macOS/Linux:**
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate
```

**Windows:**
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
.\venv\Scripts\activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Run the Application
```bash
streamlit run streamlit_app.py
```
- Automatically opens in your browser at `http://localhost:8501`
- Modern, intuitive interface for Git operations
- Real-time Git status monitoring

## Usage

### Available Operations

1. **Git History**: Visualize commit history with interactive graphs
2. **Commit**: Create standardized commit messages with structured templates
3. **Merge**: Safely merge branches with conflict detection
4. **Create Branch**: Create new branches from existing ones
5. **Pull**: Synchronize with remote repository
6. **Push**: Upload local changes to remote repository
7. **Checkout Branch**: Switch between branches seamlessly

### Commit Message Format
The tool generates commit messages in the following structured format:
```
<type>: <title>
<title>: <title>
<body>: <description>
```

**Supported Commit Types:**
- `feat`: New features
- `fix`: Bug fixes
- `docs`: Documentation changes
- `style`: Code formatting and style changes
- `refactor`: Code refactoring
- `test`: Test additions or modifications
- `chore`: Build process or auxiliary tool changes
- `build`: Build system or external dependency changes

### Why Standardized Commits?
- **Better Git History**: Easier to understand project evolution
- **Automated Changelog**: Generate release notes automatically
- **Team Consistency**: Uniform commit messages across the team
- **Semantic Versioning**: Support for semantic versioning workflows
- **Issue Tracking**: Better integration with issue tracking systems

## Important Notes

- **Git Repository Required**: This tool must be run in an initialized Git repository
- **Git Configuration**: Ensure Git user information is properly configured
- **Permissions**: Verify appropriate permissions for remote repository operations
- **Conflict Resolution**: Be prepared to resolve merge conflicts when they occur

## Troubleshooting

### Common Issues

1. **"Not a Git repository" Error**
   - Verify current directory is a Git repository
   - Run `git init` to initialize a new repository

2. **Package Installation Errors**
   - Ensure virtual environment is activated
   - Run `pip install --upgrade pip` before retrying

3. **Graphviz-related Issues**
   - If graphs don't display: `pip install graphviz`
   - System Graphviz installation required (macOS: `brew install graphviz`, Ubuntu: `sudo apt-get install graphviz`)

4. **Permission Errors**
   - Configure Git user info: `git config --global user.name "Your Name"`, `git config --global user.email "your.email@example.com"`
   - Verify SSH keys or personal access tokens for remote access

## Benefits

### For Individual Developers
- **Faster Workflow**: Create commits and manage branches without command line
- **Consistent Quality**: Never forget commit message structure
- **Visual Feedback**: See repository state at a glance
- **Error Prevention**: Built-in validation and conflict detection

### For Teams
- **Standardized Process**: Everyone follows the same commit conventions
- **Better Collaboration**: Clear commit history improves code review
- **Automated Workflows**: Structured commits enable CI/CD integration
- **Reduced Conflicts**: Better merge strategies and conflict resolution

## License

This project is distributed under the MIT License.
</div>

<div id="korean-content" style="display: none;">
Git 저장소 관리를 위한 웹 기반 도구로, Streamlit을 사용한 현대적이고 직관적인 인터페이스를 제공합니다. 정형화된 커밋 메시지 생성, 브랜치 관리, Git 히스토리 시각화 등의 기능을 제공합니다.

## 주요 기능

### 📝 정형화된 커밋 메시지
- **Conventional Commit 형식**: feat, fix, docs, style, refactor, test, chore, build 타입 지원
- **구조화된 템플릿**: 제목, 본문, 타입 섹션으로 자동 포맷팅
- **일관된 히스토리**: 팀 전체의 깔끔하고 읽기 쉬운 Git 히스토리 유지
- **쉬운 커스터마이징**: 프로젝트 규칙에 맞게 커밋 타입과 템플릿 수정

### 🌿 고급 브랜치 관리
- **원활한 브랜치 작업**: 몇 번의 클릭으로 브랜치 생성, 체크아웃, 머지
- **시각적 브랜치 상태**: 현재 브랜치, 원격 상태, 커밋 차이점 실시간 표시
- **안전한 머지 작업**: 충돌 감지 및 해결 가이드와 함께 브랜치 머지
- **원격 동기화**: 명확한 상태 피드백과 함께 변경사항 Pull/Push

### 📊 Git 히스토리 시각화
- **인터랙티브 Git 그래프**: Graphviz 기반 다이어그램으로 커밋 히스토리 시각화
- **커밋 상세 정보**: 작성자, 날짜, 전체 메시지 본문을 포함한 포괄적인 커밋 정보 표시
- **브랜치 및 태그 표시**: 각 커밋을 가리키는 모든 참조 확인
- **실시간 업데이트**: 새로고침하여 최신 변경사항 즉시 확인

### 🎯 현대적인 웹 인터페이스
- **직관적인 디자인**: 깔끔하고 반응형 Streamlit 인터페이스
- **사이드바 네비게이션**: 모든 Git 작업에 빠른 접근
- **실시간 상태**: 저장소 상태의 실시간 업데이트
- **크로스 플랫폼**: macOS, Linux, Windows 지원

## 환경 요구사항

- Python 3.7 이상
- Git
- macOS/Linux/Windows 지원

## 설치 및 실행

### 1. 프로젝트 파일 복사
다음 파일들을 대상 Git 저장소에 복사하세요:

**필수 파일:**
- `streamlit_app.py` - 메인 Streamlit 애플리케이션
- `git_utils.py` - Git 유틸리티 함수들
- `requirements.txt` - Python 의존성 패키지

**복사 방법:**
```bash
# 방법 1: 파일들을 직접 복사
cp streamlit_app.py /path/to/your/git/repository/
cp git_utils.py /path/to/your/git/repository/
cp requirements.txt /path/to/your/git/repository/

# 방법 2: 전체 프로젝트를 복사 후 필요한 파일만 추출
cp -r commit-frame /path/to/your/git/repository/
cd /path/to/your/git/repository/commit-frame
# 필요한 파일들을 상위 디렉토리로 이동
```

### 2. 저장소 클론 (원본 저장소에서 작업하는 경우)
```bash
git clone [repository-url]
cd commit-frame
```

### 3. 가상환경 생성 및 활성화

**macOS/Linux:**
```bash
# 가상환경 생성
python3 -m venv venv

# 가상환경 활성화
source venv/bin/activate
```

**Windows:**
```bash
# 가상환경 생성
python -m venv venv

# 가상환경 활성화
.\venv\Scripts\activate
```

### 4. 의존성 패키지 설치
```bash
pip install -r requirements.txt
```

### 5. 애플리케이션 실행
```bash
streamlit run streamlit_app.py
```
- 브라우저에서 자동으로 `http://localhost:8501`로 접속됩니다
- Git 작업을 위한 현대적이고 직관적인 인터페이스
- 실시간 Git 상태 모니터링

## 사용법

### 사용 가능한 작업

1. **Git History**: 인터랙티브 그래프로 커밋 히스토리 시각화
2. **Commit**: 구조화된 템플릿으로 정형화된 커밋 메시지 생성
3. **Merge**: 충돌 감지와 함께 안전하게 브랜치 머지
4. **Create Branch**: 기존 브랜치에서 새 브랜치 생성
5. **Pull**: 원격 저장소와 동기화
6. **Push**: 로컬 변경사항을 원격 저장소에 업로드
7. **Checkout Branch**: 브랜치 간 원활한 전환

### 커밋 메시지 형식
도구는 다음 구조화된 형식으로 커밋 메시지를 생성합니다:
```
<type>: <title>
<title>: <title>
<body>: <description>
```

**지원하는 커밋 타입:**
- `feat`: 새로운 기능
- `fix`: 버그 수정
- `docs`: 문서 변경
- `style`: 코드 포맷팅 및 스타일 변경
- `refactor`: 코드 리팩토링
- `test`: 테스트 추가 또는 수정
- `chore`: 빌드 프로세스 또는 보조 도구 변경
- `build`: 빌드 시스템 또는 외부 종속성 변경

### 정형화된 커밋의 장점
- **더 나은 Git 히스토리**: 프로젝트 진화를 더 쉽게 이해
- **자동화된 변경 로그**: 릴리스 노트 자동 생성
- **팀 일관성**: 팀 전체의 균일한 커밋 메시지
- **시맨틱 버저닝**: 시맨틱 버저닝 워크플로우 지원
- **이슈 트래킹**: 이슈 트래킹 시스템과의 더 나은 통합

## 주의사항

- **Git 저장소 필수**: 이 도구는 초기화된 Git 저장소에서 실행해야 합니다
- **Git 설정**: Git 사용자 정보가 올바르게 설정되어 있는지 확인
- **권한 확인**: 원격 저장소 작업을 위한 적절한 권한 확인
- **충돌 해결**: 머지 작업 시 충돌이 발생할 수 있으니 주의하세요

## 문제 해결

### 일반적인 문제들

1. **"Not a Git repository" 오류**
   - 현재 디렉토리가 Git 저장소인지 확인
   - `git init` 명령어로 새 저장소 초기화

2. **패키지 설치 오류**
   - 가상환경이 활성화되어 있는지 확인
   - `pip install --upgrade pip` 실행 후 재시도

3. **Graphviz 관련 오류**
   - 그래프가 표시되지 않는 경우: `pip install graphviz` 실행
   - 시스템 Graphviz 설치 필요 (macOS: `brew install graphviz`, Ubuntu: `sudo apt-get install graphviz`)

4. **권한 오류**
   - Git 사용자 정보 설정: `git config --global user.name "Your Name"`, `git config --global user.email "your.email@example.com"`
   - 원격 접근을 위한 SSH 키 또는 개인 액세스 토큰 확인

## 혜택

### 개인 개발자를 위한
- **더 빠른 워크플로우**: 명령줄 없이 커밋 생성 및 브랜치 관리
- **일관된 품질**: 커밋 메시지 구조를 절대 잊지 않음
- **시각적 피드백**: 저장소 상태를 한눈에 확인
- **오류 방지**: 내장된 검증 및 충돌 감지

### 팀을 위한
- **표준화된 프로세스**: 모든 사람이 동일한 커밋 규칙을 따름
- **더 나은 협업**: 명확한 커밋 히스토리가 코드 리뷰를 개선
- **자동화된 워크플로우**: 구조화된 커밋이 CI/CD 통합을 가능하게 함
- **충돌 감소**: 더 나은 머지 전략 및 충돌 해결

## 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다.
</div>

<script>
function toggleLanguage() {
    const englishContent = document.getElementById('english-content');
    const koreanContent = document.getElementById('korean-content');
    const langBtn = document.getElementById('langBtn');
    
    if (englishContent.style.display === 'none') {
        // Switch to English
        englishContent.style.display = 'block';
        koreanContent.style.display = 'none';
        langBtn.textContent = '한국어';
    } else {
        // Switch to Korean
        englishContent.style.display = 'none';
        koreanContent.style.display = 'block';
        langBtn.textContent = 'English';
    }
}

// Set initial language based on browser preference
document.addEventListener('DOMContentLoaded', function() {
    const userLang = navigator.language || navigator.userLanguage;
    if (userLang.startsWith('ko')) {
        toggleLanguage(); // Switch to Korean if browser language is Korean
    }
});
</script>
