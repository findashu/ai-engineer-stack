# Virtual Environments & Code Style

Dependencies are the #1 source of "works on my machine" bugs. Virtual environments solve this by giving each project its own isolated Python with its own packages.

---
 
## The Problem They Solve
 
```
Without venv:                          With venv:
 
System Python                          System Python
└── requests 2.28                      ├── Project A (.venv)
└── flask 2.0                          │   └── requests 2.28, flask 2.0
└── numpy 1.23                         └── Project B (.venv)
                                           └── requests 2.31, flask 3.0
Project A needs flask 2.0 ✅                    (no conflict)
Project B needs flask 3.0 ❌ CONFLICT
```
 
Every project gets its own isolated copy of Python + packages — no conflicts, no surprises.
 
---

## What's Inside a Virtual Environment
 
```
.venv/
├── bin/
│   ├── python3         ← symlink to your Python version
│   ├── pip             ← pip tied to this venv only
│   └── activate        ← shell script that activates the venv
├── lib/
│   └── python3.x/
│       └── site-packages/   ← all your installed packages go here
└── pyvenv.cfg          ← records which Python version this venv uses
```
 
When you `activate`, it temporarily prepends `.venv/bin` to your `$PATH` — so `python3` and `pip` resolve to the venv versions, not the system ones.
 
---

## The Standard Way: `venv`
 
Built into Python 3 — no extra install needed.

### Create
 
```bash
# Inside your project folder
python3 -m venv .venv
```
 
> Use `.venv` (with dot) — the dot hides it in file explorers and it's the most widely recognised convention. Some teams use `venv` without the dot — pick one and be consistent.
 
### Activate
 
```bash
# macOS / Linux
source .venv/bin/activate
 
# Windows (Command Prompt)
.venv\Scripts\activate.bat
 
# Windows (PowerShell)
.venv\Scripts\Activate.ps1
```
 
Your prompt changes to show the active environment:
```
(.venv) ashutosh@MacBook project %
```
 
### Verify it's active
 
```bash
which python3           # should show .../project/.venv/bin/python3
python3 -m pip --version  # confirms pip is from the venv
```
 
### Install packages
 
```bash
pip install flask
pip install requests==2.31.0    # pin to exact version
pip install "flask>=2.0,<3.0"   # version range
```
 
### Deactivate
 
```bash
deactivate
```
 
---

## Managing Dependencies
 
### `requirements.txt` — the standard approach
 
```bash
# Export current environment's packages with exact versions
pip freeze > requirements.txt
```
 
```
# requirements.txt — example output
flask==3.0.2
requests==2.31.0
click==8.1.7
```
 
```bash
# Recreate the environment on another machine
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
 
> 💡 **Tip:** `pip freeze` captures **everything** including transitive dependencies (packages your packages depend on). This is good for locking exact reproducible builds, but makes the file noisy. Consider maintaining a lean `requirements.in` with only your direct dependencies, and using `pip-tools` to compile the full lockfile:
> ```bash
> pip install pip-tools
> pip-compile requirements.in   # generates requirements.txt with all pins
> pip-sync requirements.txt     # installs exactly what's in the lockfile
> ```
 
### Dev vs Prod dependencies
 
Keep them separate — you don't want `pytest` and `black` going to production:
 
```
requirements.txt          ← production only
requirements-dev.txt      ← dev tools (testing, linting, formatting)
```
 
```bash
# requirements-dev.txt
-r requirements.txt       # include prod deps
pytest==8.1.1
black==24.3.0
ruff==0.4.0
```
 
```bash
pip install -r requirements-dev.txt   # local dev setup
pip install -r requirements.txt       # production / CI
```
 
---
 
## `.gitignore` — what to commit, what to ignore
 
```gitignore
# Never commit the venv itself — it's machine-specific
.venv/
venv/
__pycache__/
*.pyc
*.pyo
.DS_Store         # macOS specific
 
# DO commit these
# requirements.txt
# requirements-dev.txt
# .python-version   (if using pyenv)
```
 
---
 
## Modern Alternative: `uv` (2024+)
 
`uv` is a next-generation Python package and environment manager — written in Rust, significantly faster than pip + venv.
 
```bash
# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh
 
# Create venv + install packages in one step
uv venv
uv pip install flask requests
 
# Install from requirements.txt
uv pip install -r requirements.txt
 
# Sync exact lockfile (like pip-sync)
uv pip sync requirements.txt
```
 
| | `venv` + `pip` | `uv` |
|---|---|---|
| Speed | Baseline | 10–100x faster |
| Built-in lockfile | No (need pip-tools) | Yes |
| Needs install | No (stdlib) | Yes (one-time) |
| Maturity | Stable, universal | Newer, rapidly adopted |
 
> 💡 **Tip:** `uv` is worth learning now — it's being adopted fast in production Python projects. But understand `venv` + `pip` first, since you'll encounter them in every existing codebase.
 
---
 
## Code Style: PEP 8
 
PEP 8 is Python's official style guide. Following it makes your code readable to any Python developer.
 
### Core rules
 
```python
# ✅ Indentation — 4 spaces, never tabs
def greet(name):
    print(f"Hello, {name}")
 
# ✅ Naming conventions
my_variable = 10          # snake_case for variables and functions
MY_CONSTANT = 100         # UPPER_SNAKE_CASE for constants
class MyClassName:  pass  # PascalCase for classes
 
# ✅ Line length — 79 chars (PEP 8) or 88 chars (Black's default)
# Break long lines:
result = (
    first_value
    + second_value
    + third_value
)
 
# ✅ Blank lines — 2 between top-level definitions, 1 inside a class
def function_one():
    pass
 
 
def function_two():
    pass
 
 
# ✅ Imports — stdlib first, then third-party, then local
import os
import sys
 
import requests
import flask
 
from mymodule import helper
```
 
### Automate it — don't manually fix style
 
```bash
pip install black ruff
 
black .          # auto-formats your code (opinionated, no config needed)
ruff check .     # fast linter — catches bugs and style issues
ruff check --fix .  # auto-fix what it can
```
 
| Tool | What it does |
|---|---|
| `black` | Auto-formatter — rewrites your code to be PEP 8 compliant |
| `ruff` | Fast linter — catches errors, unused imports, bad patterns |
| `autopep8` | Older formatter, less opinionated than black |
| `flake8` | Older linter, still widely used |
 
> 💡 **Tip:** Add `black` and `ruff` to your editor's format-on-save. Never think about style manually again. In team projects, enforce it in CI so style debates don't happen in code review.
 
---
 
## Recommended Project Structure
 
```
my_project/
├── .venv/                  ← virtual environment (gitignored)
├── .gitignore
├── .python-version         ← pyenv version pin (e.g. "3.12.3")
├── requirements.txt        ← production dependencies
├── requirements-dev.txt    ← dev dependencies
├── README.md
└── src/
    └── main.py
```
 
---
 
## Quick Reference
 
```bash
python3 -m venv .venv               # create venv
source .venv/bin/activate           # activate (macOS)
which python3                       # verify venv is active
pip install <package>               # install package
pip freeze > requirements.txt       # export dependencies
pip install -r requirements.txt     # install from file
deactivate                          # exit venv
black .                             # format code
ruff check .                        # lint code
```
 
---
 
## Key Takeaways
 
- One virtual environment per project — always. No exceptions.
- `.venv/` goes in `.gitignore`; `requirements.txt` gets committed.
- `pip freeze` pins everything including transitive deps — use `pip-tools` for cleaner dependency management on real projects.
- Separate dev and prod requirements from the start.
- Use `black` + `ruff` and stop thinking about style manually.
- `uv` is the future — worth knowing, but learn `venv` + `pip` first.
 