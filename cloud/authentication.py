import jwt
from django.conf import settings
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed


class PlatformPrincipal:
    def __init__(self, claims):
        self.id = claims["sub"]
        self.claims = claims
        self.is_authenticated = True


class PlatformJWTAuthentication(BaseAuthentication):
    jwks_client = jwt.PyJWKClient(settings.JWT_JWKS_URL, cache_keys=True, lifespan=300)

    def authenticate(self, request):
        token = request.COOKIES.get(settings.ACCESS_COOKIE_NAME)
        authorization = request.headers.get("Authorization", "")
        if not token and authorization.startswith("Bearer "):
            token = authorization.removeprefix("Bearer ").strip()
        if not token:
            return None
        try:
            signing_key = self.jwks_client.get_signing_key_from_jwt(token)
            claims = jwt.decode(
                token, signing_key.key, algorithms=["RS256"],
                audience=settings.JWT_AUDIENCE, issuer=settings.JWT_ISSUER,
            )
        except jwt.PyJWTError as exc:
            raise AuthenticationFailed("Invalid or expired access token") from exc
        return PlatformPrincipal(claims), claims

