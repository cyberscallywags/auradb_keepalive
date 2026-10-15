# 🏴‍☠️ Cyber Scallywags — Project Template

A standalone, batteries-included starter template for new **Cyber Scallywags**
projects. Copy this directory into a fresh repository and you get a documented
README, license, community-health docs, CI/CD pipelines, and issue/PR templates
out of the box.

## What's inside

```text
project-template/
├── README.template.md           → rename to README.md (badges + full section set)
├── LICENSE                      → MIT license (fill in {{YEAR}} / {{AUTHOR}})
├── .gitignore                   → sensible defaults (secrets, build, OS, IDE)
├── .env.example                 → document your env vars here; never commit .env
├── CONTRIBUTING.md              → how to contribute
├── CODE_OF_CONDUCT.md           → Contributor Covenant
├── SECURITY.md                  → private vulnerability disclosure policy
├── .gitlab-ci.yml               → GitLab CI pipeline (lint + test + build)
└── .github/
    ├── workflows/ci.yml         → GitHub Actions: lint + test + Docker build
    ├── workflows/codeql.yml     → GitHub Actions: CodeQL security scan
    ├── dependabot.yml           → automated dependency updates
    ├── PULL_REQUEST_TEMPLATE.md → PR checklist
    └── ISSUE_TEMPLATE/          → bug report + feature request forms
```

## How to bootstrap a new project

```bash
# 1. Copy the template contents into your new repo root
cp -r project-template/. /path/to/new-repo/
cd /path/to/new-repo

# 2. Rename the README template into place
mv README.template.md README.md

# 3. Replace the placeholders across all files
#    {{PROJECT_NAME}} {{REPO}} {{TAGLINE}} {{DEFAULT_BRANCH}}
#    {{CI_WORKFLOW_FILE}} {{LANG}} {{YEAR}} {{AUTHOR}}
grep -rl '{{' . | xargs sed -i \
  -e 's/{{PROJECT_NAME}}/My Project/g' \
  -e 's/{{REPO}}/my-repo/g' \
  -e 's/{{DEFAULT_BRANCH}}/main/g' \
  -e 's/{{CI_WORKFLOW_FILE}}/ci.yml/g' \
  -e 's/{{LANG}}/python/g' \
  -e 's/{{YEAR}}/2026/g' \
  -e 's/{{AUTHOR}}/cyberscallywags/g'
#    (set {{TAGLINE}} by hand — it's prose)

# 4. Trim anything that doesn't apply, then commit
git init && git add -A && git commit -m "chore: bootstrap from Cyber Scallywags template"
```

> **Tip:** you can also turn this into a GitHub [template repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-template-repository)
> so new repos can be created from it with one click.

## Placeholders

| Placeholder          | Meaning                                  | Example             |
| -------------------- | ---------------------------------------- | ------------------- |
| `{{PROJECT_NAME}}`   | Human-readable project name              | `AuraDB Keep-Alive` |
| `{{REPO}}`           | GitHub repo name (owner is always `cyberscallywags`) | `auradb_keepalive` |
| `{{TAGLINE}}`        | One-line description                      | prose               |
| `{{DEFAULT_BRANCH}}` | Default branch                            | `main`              |
| `{{CI_WORKFLOW_FILE}}` | CI workflow filename                    | `ci.yml`            |
| `{{LANG}}`           | Primary language                          | `python`            |
| `{{YEAR}}`           | Copyright year                            | `2026`              |
| `{{AUTHOR}}`         | Copyright holder                          | `cyberscallywags`   |

Everything here is a starting point — keep what helps, delete what doesn't.
