# Virtual Environments

This section covers Python virtual environments, which are essential for managing project dependencies and avoiding conflicts between different projects.

## What is a Virtual Environment?

A virtual environment is an isolated Python environment that allows you to install packages for a specific project without affecting the system Python installation or other projects.

**Always work in a virtual environment** for Python projects to maintain clean, reproducible setups.

## Traditional Way: venv

### Creating a Virtual Environment

```bash
python3 -m venv .venv
```

This creates a `.venv` directory in your current folder containing the virtual environment.

### Activating the Virtual Environment

```bash
source .venv/bin/activate
```

Your prompt should now show `(.venv)` indicating the environment is active.

### Deactivating

```bash
deactivate
```

### Installing Packages

With the environment activated:

```bash
pip install flask
pip install requests
```

### Requirements.txt

A `requirements.txt` file lists all dependencies for a project. Create one with:

```bash
pip freeze > requirements.txt
```

Install from requirements.txt:

```bash
pip install -r requirements.txt
```

Example `requirements.txt`:
```
requests
flask
```

## Best Practices

- Always activate your virtual environment before working on a project
- Use descriptive names for virtual environments (e.g., `.venv` or `venv`)
- Commit `requirements.txt` to version control, not the virtual environment folder
- Use `pip freeze` to capture exact versions after testing

## Code Style: PEP 8

Follow Python's style guide for clean, readable code:

- Use 4 spaces for indentation (never tabs)
- Use descriptive variable and function names
- Maximum line length: 79 characters
- Use formatters like `black` or `autopep8`

## Modern Alternatives

In upcoming sections, we'll explore modern tools like `uv` for faster virtual environment and package management.

## Next Steps

- Practice creating and using virtual environments
- Move to [Data Types](../03-datatypes/README.md) to understand Python's type system