# Getting Started

Get {{PROJECT_NAME}} running in a few minutes.

## Prerequisites

- {{LANG}} >= `X.Y`
- Docker & Docker Compose _(optional)_
- Any required accounts / API keys

## 1. Clone

```bash
git clone https://github.com/cyberscallywags/{{REPO}}.git
cd {{REPO}}
```

## 2. Configure

```bash
cp .env.example .env
# edit .env and fill in your values
```

See **[Configuration](Configuration)** for every available setting.

## 3. Install & run

```bash
# install deps (python)
pip install -r requirements.txt

# run
python app.py
```

Or with Docker:

```bash
docker compose up -d --build
```

## Next steps

- **[Usage](Usage)** — common tasks and examples
- **[Architecture](Architecture)** — understand how it works
- **[Troubleshooting](Troubleshooting)** — if something doesn't work
