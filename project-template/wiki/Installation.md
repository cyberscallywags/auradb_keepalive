# Installation

Detailed installation options for {{PROJECT_NAME}}.

## Option A — Local ({{LANG}})

```bash
git clone https://github.com/cyberscallywags/{{REPO}}.git
cd {{REPO}}
pip install -r requirements.txt     # or: npm install
```

## Option B — Docker

```bash
docker build -t {{REPO}} .
docker run --rm --env-file .env {{REPO}}
```

## Option C — Docker Compose

```bash
docker compose up -d --build
```

## Verifying the install

```bash
# e.g. run the health check / version command
python health_check.py    # adjust to your project
```

You should see a success message. If not, see **[Troubleshooting](Troubleshooting)**.

## Upgrading

```bash
git pull
pip install -r requirements.txt --upgrade
# or rebuild the image: docker compose up -d --build
```
