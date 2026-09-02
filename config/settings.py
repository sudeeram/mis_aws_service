import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "unsafe-aws-development-key")
DEBUG = os.getenv("DJANGO_DEBUG", "true").lower() == "true"
ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "*").split(",")
INSTALLED_APPS = [
    "django.contrib.auth", "django.contrib.contenttypes", "django.contrib.staticfiles",
    "rest_framework", "cloud",
]
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.middleware.common.CommonMiddleware",
    "cloud.middleware.CorrelationIdMiddleware",
]
ROOT_URLCONF = "config.urls"
WSGI_APPLICATION = "config.wsgi.application"
DATABASES = {"default": {
    "ENGINE": "django.db.backends.postgresql",
    "NAME": os.getenv("POSTGRES_DB", "aws"),
    "USER": os.getenv("POSTGRES_USER", "aws"),
    "PASSWORD": os.getenv("POSTGRES_PASSWORD", "aws-dev-password"),
    "HOST": os.getenv("POSTGRES_HOST", "aws-postgres"),
    "PORT": os.getenv("POSTGRES_PORT", "5432"),
}}
if os.getenv("USE_SQLITE_FOR_TESTS", "false").lower() == "true":
    DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": BASE_DIR / "test.sqlite3"}}
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
JWT_ISSUER = os.getenv("JWT_ISSUER", "http://platform.local/api/auth")
JWT_AUDIENCE = os.getenv("JWT_AUDIENCE", "platform-api")
JWT_JWKS_URL = os.getenv("JWT_JWKS_URL", "http://auth-service:8000/api/auth/.well-known/jwks.json")
ACCESS_COOKIE_NAME = "platform_access"
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": ["cloud.authentication.PlatformJWTAuthentication"],
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.IsAuthenticated"],
    "EXCEPTION_HANDLER": "cloud.exceptions.api_exception_handler",
}
