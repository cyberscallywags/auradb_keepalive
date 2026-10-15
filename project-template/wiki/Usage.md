# Usage

How to run {{PROJECT_NAME}} and perform common tasks.

## Running

```bash
# foreground
python app.py

# with Docker Compose (detached)
docker compose up -d
```

## Common tasks

### Task one

```bash
# command + short explanation
```

### Task two

```bash
# command + short explanation
```

## Logs

```bash
# local
tail -f app.log

# docker compose
docker compose logs -f
```

## Stopping

```bash
# Ctrl+C for foreground, or:
docker compose down
```

## Tips

- Set `LOG_LEVEL=DEBUG` for verbose output while diagnosing issues.
- See **[Configuration](Configuration)** for all tunable settings.
