from django.test import TestCase
from rest_framework.test import APIRequestFactory

from .permissions import HasFeaturePermission
from .serializers import AwsConnectionSerializer
from .views import DashboardView


class PermissionTests(TestCase):
    def test_feature_permission_is_required(self):
        request = APIRequestFactory().get("/api/aws/dashboard")
        request.auth = {"permissions": []}
        self.assertFalse(HasFeaturePermission().has_permission(request, DashboardView()))
        request.auth = {"permissions": ["aws:dashboard:view"]}
        self.assertTrue(HasFeaturePermission().has_permission(request, DashboardView()))

    def test_account_id_validation(self):
        serializer = AwsConnectionSerializer(data={
            "name": "Development", "aws_account_id": "123", "default_region": "us-east-1",
            "authentication_method": "DEVELOPMENT", "status": "UNVERIFIED",
        })
        self.assertFalse(serializer.is_valid())
        self.assertIn("aws_account_id", serializer.errors)
