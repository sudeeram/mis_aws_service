import uuid
from django.db import models


class AwsConnection(models.Model):
    class Status(models.TextChoices):
        UNVERIFIED = "UNVERIFIED", "Unverified"
        ACTIVE = "ACTIVE", "Active"
        DISABLED = "DISABLED", "Disabled"

    class AuthenticationMethod(models.TextChoices):
        IAM_ROLE = "IAM_ROLE", "IAM role"
        DEVELOPMENT = "DEVELOPMENT", "Development placeholder"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=120)
    aws_account_id = models.CharField(max_length=12)
    default_region = models.CharField(max_length=32)
    authentication_method = models.CharField(max_length=24, choices=AuthenticationMethod.choices, default=AuthenticationMethod.DEVELOPMENT)
    status = models.CharField(max_length=16, choices=Status.choices, default=Status.UNVERIFIED)
    created_by_user_id = models.UUIDField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("name",)

