# AuraDB Keep-Alive

[![CI](https://github.com/cyberscallywags/auradb_keepalive/actions/workflows/ci.yml/badge.svg)](https://github.com/cyberscallywags/auradb_keepalive/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/docker-ready-2496ED.svg?logo=docker&logoColor=white)](https://www.docker.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A tiny, containerised watchdog that keeps a [Neo4j AuraDB](https://neo4j.com/cloud/aura/) instance from being paused for inactivity. It runs a lightweight query on a schedule and optionally alerts you via Slack or email when the database is unreachable.

> **Why?** Free-tier and idle AuraDB instances are automatically paused after a period of inactivity. A periodic no-op query keeps the instance warm.

## How it works

- `keep_alive.py` connects to AuraDB and runs `RETURN datetime()` every `FREQUENCY_MINUTES`.
- On connection/auth failure it fires optional Slack and/or email alerts.
- `health_check.py` is used as the container `HEALTHCHECK` — it opens a session, runs `RETURN 1`, and exits non-zero on failure.

## Configuration

All configuration is via environment variables.

| Variable            | Default                                        | Description                                   |
| ------------------- | ---------------------------------------------- | --------------------------------------------- |
| `AURA_URI`          | `neo4j+s://<your-instance-id>.databases.neo4j.io` | AuraDB connection URI                      |
| `AURA_USER`         | `neo4j`                                         | Database username                             |
| `AURA_PASSWORD`     | `<your-password>`                               | Database password                             |
| `FREQUENCY_MINUTES` | `500`                                           | Minutes between keep-alive queries            |
| `ENABLE_SLACK`      | `false`                                         | Enable Slack alerts on failure                |
| `SLACK_WEBHOOK`     | _(empty)_                                       | Slack incoming webhook URL                    |
| `ENABLE_EMAIL`      | `false`                                         | Enable email alerts on failure                |
| `SMTP_SERVER`       | `smtp.gmail.com`                                | SMTP server host                              |
| `SMTP_PORT`         | `587`                                           | SMTP server port                              |
| `SMTP_USER`         | _(empty)_                                       | SMTP username / from address                  |
| `SMTP_PASSWORD`     | _(empty)_                                       | SMTP password                                 |
| `EMAIL_TO`          | _(empty)_                                       | Recipient address for alerts                  |

> **Security:** Never commit real credentials. Provide secrets at runtime via a `.env` file (git-ignored), Docker secrets, or your CI/CD platform's secret store.

## Quick start

### Docker Compose

```bash
# Set your credentials via environment / .env, then:
docker compose up -d --build
```

### Docker

```bash
docker build -t auradb-keepalive .
docker run -d --restart unless-stopped \
  -e AURA_URI="neo4j+s://<your-instance-id>.databases.neo4j.io" \
  -e AURA_USER="neo4j" \
  -e AURA_PASSWORD="<your-password>" \
  -e FREQUENCY_MINUTES=500 \
  --name auradb_keepalive \
  auradb-keepalive
```

### Local (Python)

```bash
pip install -r requirements.txt
export AURA_URI="neo4j+s://<your-instance-id>.databases.neo4j.io"
export AURA_USER="neo4j"
export AURA_PASSWORD="<your-password>"
python keep_alive.py
```

## CI/CD

Pipelines are provided for both platforms and run linting + a Docker build on every push / merge request:

- **GitHub Actions** — [`.github/workflows/ci.yml`](.github/workflows/ci.yml)
- **GitLab CI** — [`.gitlab-ci.yml`](.gitlab-ci.yml)

To display the CI badge above, replace `cyberscallywags/auradb_keepalive` in the badge URLs with your own `owner/repo` if you fork this project.

## License

Released under the [MIT License](LICENSE).
