# Configuration

{{PROJECT_NAME}} is configured via environment variables. Copy `.env.example`
to `.env` and set values there — **never commit real secrets**.

## Environment variables

| Variable        | Required | Default   | Description                  |
| --------------- | :------: | --------- | ---------------------------- |
| `EXAMPLE_URL`   |    ✅     | —         | Service endpoint             |
| `EXAMPLE_TOKEN` |    ✅     | —         | Auth token / API key         |
| `LOG_LEVEL`     |    ❌     | `INFO`    | Logging verbosity            |
| `ENABLE_FEATURE_X` | ❌    | `false`   | Toggle for feature X         |

## Where configuration comes from

Precedence (highest wins):

1. Explicit environment variables (e.g. set in your shell or CI)
2. Values in `.env`
3. Built-in defaults

## Secrets management

- **Local:** use a git-ignored `.env` file.
- **CI/CD:** use the platform's secret store (GitHub Actions secrets, GitLab
  CI/CD variables) — never hard-code secrets in workflow files.
- **Production:** inject via your orchestrator (Docker secrets, Kubernetes
  secrets, a vault), not baked into images.

> If a secret is ever committed, treat it as compromised: rotate it and purge
> it from git history. See the repo's `SECURITY.md`.
