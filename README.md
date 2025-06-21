# Git Commit/Merge Formatter

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
