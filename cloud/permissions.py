from rest_framework.permissions import BasePermission


class HasFeaturePermission(BasePermission):
    def has_permission(self, request, view):
        required = getattr(view, "required_permission", None)
        claims = request.auth or {}
        return required is None or required in claims.get("permissions", [])

