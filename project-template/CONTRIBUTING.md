# Contributing to {{PROJECT_NAME}}

First off — thanks for taking the time to contribute! 🏴‍☠️

## Code of Conduct

This project is governed by our [Code of Conduct](CODE_OF_CONDUCT.md). By
participating, you are expected to uphold it.

## How can I contribute?

### 🐛 Reporting bugs

- Search [existing issues](https://github.com/cyberscallywags/{{REPO}}/issues) first.
- If it's new, open a bug report with clear steps to reproduce, expected vs.
  actual behaviour, and your environment.

### 💡 Suggesting features

- Open a feature request describing the problem you're solving, not just the
  solution you have in mind.

### 🔧 Pull requests

1. Fork the repo and create a branch from `{{DEFAULT_BRANCH}}`:
   `git checkout -b feature/short-description`
2. Make your changes with clear, focused commits.
3. Add or update tests and documentation as needed.
4. Ensure lint and tests pass locally (see below).
5. Open a PR against `{{DEFAULT_BRANCH}}` and fill in the PR template.

## Development setup

```bash
git clone https://github.com/cyberscallywags/{{REPO}}.git
cd {{REPO}}
# install deps, e.g. pip install -r requirements.txt  /  npm install
```

## Checks before you push

```bash
ruff check .        # lint
ruff format .       # format
pytest -q           # tests   (or: npm test)
```

## Commit messages

We prefer [Conventional Commits](https://www.conventionalcommits.org/):

```
feat: add keep-alive retry with backoff
fix: handle expired auth token
docs: clarify env var defaults
```

## Coding style

- Keep changes focused and small where possible.
- Match the style of the surrounding code.
- Prefer clarity over cleverness.

Thanks again! ⭐
