# Python Basics

This section covers the fundamental prerequisites and setup for working with Python on macOS, including installation, version checking, and running Python code.

## Prerequisites

Before starting with Python development, ensure you have the following:

- macOS (latest version recommended)
- Command Line Tools for Xcode (install with `xcode-select --install`)
- Homebrew (optional, but recommended for package management)

## Installing Python

macOS comes pre-installed with Python 2.7, but for modern development, you need Python 3.

### Option 1: Using Homebrew (Recommended)

1. Install Homebrew if not already installed:
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. Install Python 3:
   ```bash
   brew install python
   ```

### Option 2: Official Python Installer

1. Download the latest Python 3 installer from [python.org](https://www.python.org/downloads/)
2. Run the installer and follow the instructions
3. Add Python to your PATH if prompted

## Verifying Installation

After installation, verify Python is working:

```bash
python3 --version
```

You should see output like: `Python 3.11.5` (version may vary)

## Running Python Code

### Interactive Mode

Start Python interactive shell:
```bash
python3
```

Exit with `Ctrl+D` or `exit()`

### Running Scripts

Create a Python file (e.g., `testpython.py`):

```python
import sys
print(sys.version)
```

Run it:
```bash
python3 testpython.py
```

## Next Steps

1. Proceed to [Virtual Environments](../02-virtual-environment/README.md)
