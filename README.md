# ai-engineer-stack

> Master the AI Engineer Stack: A professional-grade roadmap for Agentic Generative AI — covering Python, LangGraph, Multi-Agent workflows, Scalable RAG, Semantic Memory, and MCP integrations using LLMs from Hugging Face and OpenAI.
 
A structured learning repository following the **Full Stack Generative and Agentic AI with Python** course on Udemy. Built as a personal reference — each module's README is written to be useful long after the course is done, with real-world context and senior engineer notes alongside the fundamentals.

---

## Tech Stack
 
| Layer | Technologies |
|---|---|
| Language | Python 3.12+ |
| LLM Providers | OpenAI, Hugging Face |
| Agent Framework | LangGraph |
| Memory | Semantic Memory, Vector Stores |
| Retrieval | Scalable RAG pipelines |
| Integration | MCP (Model Context Protocol) |
| Workflow | Multi-Agent orchestration |
 
---

## What This Course Covers

The course is split into two major phases:

**Phase 1 — Python Foundations**
Get comfortable with Python as it's actually used in AI/ML engineering — not just syntax, but patterns you'll see repeatedly in real codebases.

**Phase 2 — Generative & Agentic AI**
Build real AI systems — from raw LLM API calls through to autonomous multi-agent workflows with persistent memory, tool use, and scalable retrieval.

---

## Repository Structure

```
ai-engineer-stack/
├── 01-python/
│   ├── 01-basics/
│   ├── 02-virtual-environment/
│   ├── 03-datatypes/
│   ├── 04-conditions/
│   ├── 05-loops/
│   ├── 06-function/
│   ├── 07-comprehensions/
│   ├── 08-generators-decorators/
│   ├── 09-object-oriented-programming/
│   └── 10-exception-handling/
└── 02-ai/                        ← upcoming
```

Each module contains:
- `README.md` — concepts, examples, and engineer tips
- `.py` files — working code examples referenced in the README

---

## Table of Contents

### Phase 1 — Python Foundations

| # | Topic | What You'll Learn |
|---|---|---|
| 01 | [Python Basics](01-python/01_basics/README.md) | Installation, interpreter, running scripts, venv intro |
| 02 | [Virtual Environments](01-python/02-virtual-environment/README.md) | `venv`, `pip`, dependency management, PEP 8, `uv` |
| 03 | [Data Types](01-python/03-datatypes/README.md) | Strings, numbers, lists, tuples, dicts, sets, mutability |
| 04 | [Conditions](01-python/04-conditions/README.md) | `if/elif/else`, comparison operators, ternary expressions |
| 05 | [Loops](01-python/05-loops/README.md) | `for`, `while`, `break`, `continue`, `enumerate`, `zip` |
| 06 | [Functions](01-python/06-function/Readme.md) | Args, return values, scope, `*args`/`**kwargs`, lambdas |
| 07 | [Comprehensions](01-python/07-comprehensions/README.md) | List, set, dict, generator comprehensions |
| 08 | [Generators & Decorators](01-python/08-generators-decorators/Readme.md) | Lazy iteration, `yield`, decorator pattern, `functools` |
| 09 | [Object-Oriented Programming](01-python/09-object-oriented-programming/Readme.md) | Classes, inheritance, composition, MRO, `@property` |
| 10 | [Exception Handling & File I/O](01-python/10-exception-handling/Readme.md) | `try/except/else/finally`, custom exceptions, safe file handling |

### Phase 2 — Generative & Agentic AI (upcoming)

---

## Prerequisites

- **macOS** (all commands shown for macOS — Linux/Windows users adapt shell commands as needed)
- Basic command line comfort
- Internet connection for installations

No prior AI/ML experience needed — the course builds it up from scratch.

---

## Getting Started

```bash
# Clone the repo
git clone https://github.com/<your-username>/ai-engineer-stack.git
cd ai-engineer-stack

# Start with Python basics if you're new
open 01-python/01_basics/README.md

# Each module has its own venv — set one up before running examples
cd 01-python/09-object-oriented-programming
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt   # if present
```

Work through modules **in order** — later modules assume knowledge from earlier ones, and the AI phase builds directly on the Python patterns covered in Phase 1.

---

## Why These READMEs Are Written This Way

Standard course notes summarise what a concept *is*. These READMEs also cover:
- **Why** it's done that way (not just how)
- **Common mistakes** and how to avoid them
- **Engineer tips** — patterns you'd only learn from real codebases
- **Quick reference tables** — useful long after the course ends