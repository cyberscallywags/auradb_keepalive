# Troubleshooting

Common problems and how to fix them. Set `LOG_LEVEL=DEBUG` for more detail.

## Problem: it won't start

**Symptoms:** process exits immediately / container restarts in a loop.

**Checks:**
- Are all required environment variables set? See **[Configuration](Configuration)**.
- Is `.env` present and readable?
- Review logs: `docker compose logs -f` or `tail -f app.log`.

## Problem: authentication / connection failures

**Symptoms:** `AuthError`, `ServiceUnavailable`, timeouts, 401/403.

**Checks:**
- Verify credentials and endpoint URL.
- Confirm the service is reachable from your network/container.
- Check for expired or rotated tokens.

## Problem: permission denied

**Checks:**
- File permissions on mounted volumes / `.env`.
- The user the container runs as.

## Problem: changes aren't taking effect

**Checks:**
- Rebuild after code changes: `docker compose up -d --build`.
- Confirm you edited the right `.env` and restarted the process.

## Still stuck?

- Search [existing issues](https://github.com/cyberscallywags/{{REPO}}/issues).
- [Open a new issue](https://github.com/cyberscallywags/{{REPO}}/issues/new/choose)
  with logs (scrub secrets first), steps to reproduce, and your environment.
