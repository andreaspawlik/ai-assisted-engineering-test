# AI-Assisted Engineering Test

A minimal example project used to practice driving development with coding
agents through a GitHub Issues backlog. The example code itself (a tiny
command-line calculator) is intentionally trivial — the focus is the
workflow: writing requirements as GitHub issues, then having an agent pick
up an issue and implement it.

## Project

`calculator` — a small Python CLI that evaluates basic arithmetic
operations. Functionality grows one GitHub issue at a time.

## Workflow

1. Requirements live as GitHub Issues in this repo (the "backlog").
2. Each issue describes one small, agent-sized unit of work (a single
   command, flag, or behavior).
3. Open an issue, then ask your coding agent to "implement issue #N",
   pointing it at this repo.
4. The agent implements the change, runs tests, and opens a PR referencing
   the issue.
5. Review, merge, close the issue, move to the next one.

## Getting started

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest
```

## Usage

```bash
python -m calculator add 2 3
```
