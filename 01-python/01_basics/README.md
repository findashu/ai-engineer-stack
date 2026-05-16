# Python Basics — Setup & First Steps

Getting Python running correctly from the start saves you hours of "it works on my machine" headaches later. This guide is **macOS-first** but the concepts apply everywhere.

---
 
## How Python Works (30-second mental model)
 
```
Your .py file  →  Python Interpreter  →  Bytecode (.pyc)  →  Output

```
 
- You write **source code** in `.py` files (plain text)
- The **interpreter** reads and executes it line by line
- Python is **dynamically typed** — no compilation step needed, errors show up at runtime
- `python3` and `python` may point to different versions on the same machine — always be explicit

---

## Prerequisites (macOS)
 
| Tool | Why you need it | Check if installed |
|---|---|---|
| Xcode Command Line Tools | Core compilers Python packages depend on | `xcode-select -p` |
| Homebrew | Package manager — install Python, tools, etc. | `brew --version` |
| Python 3.10+ | Modern Python (3.10 introduced better error messages; 3.12 is current stable) | `python3 --version` |

Install Xcode tools if missing:
```bash
xcode-select --install
```
 
---

## Installing Python
 
macOS ships with Python 2.7 (legacy, don't use it) and sometimes a system Python 3. **Don't rely on the system Python** — use your own install so you control the version.
 
### Option 1: Homebrew (Recommended for most developers)
 
```bash
# Install Homebrew if not already installed
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
 
# Install Python
brew install python
 
# Verify
python3 --version     # e.g. Python 3.12.3
which python3         # should show /opt/homebrew/bin/python3 (Apple Silicon)
                      #             /usr/local/bin/python3     (Intel Mac)
```
 
### Option 2: Official Installer (python.org)
 
1. Download from [python.org/downloads](https://www.python.org/downloads/)
2. Run the `.pkg` installer
3. Run the **"Install Certificates"** script inside the Python folder in Applications — skipping this breaks HTTPS requests
4. Verify: `python3 --version`

### Option 3: pyenv (Best for managing multiple Python versions)
 
If you'll work on multiple projects requiring different Python versions:
 
```bash
brew install pyenv
 
# Add to ~/.zshrc (macOS default shell)
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
source ~/.zshrc
 
# Install a specific version
pyenv install 3.12.3
pyenv global 3.12.3     # set as default
 
python3 --version       # Python 3.12.3
```
 
> 💡 **Tip:** Get used to `pyenv` early. Real projects pin Python versions (via `.python-version` file). Mixing system Python with project Python causes subtle, maddening bugs.
 
---

## Verifying Your Installation
 
```bash
python3 --version          # check version
which python3              # confirm which interpreter you're using
python3 -c "import sys; print(sys.executable)"   # full path to interpreter
```
 
**Watch out for this:**
```bash
python --version    # might be Python 2.7 (legacy!) or not found
python3 --version   # always use python3 explicitly
```
 
---

## Running Python Code
 
### Option 1: Interactive Shell (REPL)
 
Good for quick experiments. REPL = Read → Evaluate → Print → Loop.
 
```bash
python3
```
 
```python
>>> 2 + 2
4
>>> name = "Ashutosh"
>>> print(f"Hello, {name}")
Hello, Ashutosh
>>> exit()    # or Ctrl+D
```
 
### Option 2: Running a Script
 
```bash
# Create a file
touch hello.py
```
 
```python
# hello.py
import sys
 
print("Python version:", sys.version)
print("Interpreter path:", sys.executable)
print("Hello, World!")
```
 
```bash
python3 hello.py
```
 
### Option 3: Running Code Inline (one-liners)
 
```bash
python3 -c "print('Hello from terminal')"
python3 -c "import sys; print(sys.version)"
```
 
---
 
## Understanding `python` vs `python3` vs `pip` vs `pip3`
 
| Command | What it points to |
|---|---|
| `python` | Could be Python 2.7, Python 3, or missing — unreliable |
| `python3` | Python 3 — always use this |
| `pip` | Package installer — may match `python` (unreliable) |
| `pip3` | Package installer for Python 3 |
| `python3 -m pip` | Safest — explicitly uses the pip tied to `python3` |
 
**Always use `python3 -m pip install <package>`** to be certain you're installing into the right Python.
 
---
 
## Useful Commands Cheatsheet
 
```bash
python3 --version                   # check Python version
which python3                       # path to interpreter
python3 -m venv venv                # create virtual environment
source venv/bin/activate            # activate venv (macOS)
pip3 list                           # list installed packages
pip3 install <package>              # install a package
pip freeze > requirements.txt       # export dependencies
python3 -m pip install --upgrade pip  # upgrade pip itself
python3 -c "<code>"                 # run inline code
```
 
---
 
## Key Takeaways
 
- Use `python3` explicitly — never assume `python` points to the right version.
- Don't touch system Python — install your own via Homebrew or pyenv.
- Always use a virtual environment per project — no exceptions.
- `python3 -m pip install` is safer than `pip install` alone.
- If you'll juggle multiple Python versions → start with `pyenv` now.
 
