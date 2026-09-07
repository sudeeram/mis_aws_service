# AWS Service

## Contribution workflow

Run `./scripts/setup-git-hooks.sh` once after cloning. All work must use a
`feature/*`, `hotfix/*`, or `bugfix/*` branch. Feature and bugfix pull requests
target `develop`; hotfixes target `main` and are then merged back to `develop`.

Independent Django service for AWS-domain features. It validates platform JWTs through the auth-service JWKS endpoint and owns its MySQL database.

The skeleton stores connection metadata only. It does not store static AWS secrets or execute AWS operations.

## Local development

Copy `.env.example` to `.env`, export it in your shell, and ensure the configured
MySQL 8 database exists. The coordinated launcher is in `platform-infrastructure`.

```bash
uv sync --frozen
uv run python manage.py migrate
uv run python manage.py runserver
```

`uv` reads `.python-version`, creates an isolated `.venv`, and installs the exact
dependency versions recorded in `uv.lock`.
