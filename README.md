# AWS Service

Independent Django service for AWS-domain features. It validates platform JWTs through the auth-service JWKS endpoint and owns its PostgreSQL database.

The skeleton stores connection metadata only. It does not store static AWS secrets or execute AWS operations.

## Local development

```bash
uv sync --frozen
uv run python manage.py migrate
uv run python manage.py runserver
```

`uv` reads `.python-version`, creates an isolated `.venv`, and installs the exact
dependency versions recorded in `uv.lock`.
