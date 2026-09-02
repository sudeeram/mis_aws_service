from django.db import connection
from rest_framework import permissions, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import AwsConnection
from .permissions import HasFeaturePermission
from .serializers import AwsConnectionSerializer


class HealthLiveView(APIView):
    permission_classes = [permissions.AllowAny]
    authentication_classes = []
    def get(self, request): return Response({"status": "ok", "service": "aws"})


class HealthReadyView(HealthLiveView):
    def get(self, request):
        with connection.cursor() as cursor: cursor.execute("SELECT 1")
        return Response({"status": "ready", "service": "aws"})


class DashboardView(APIView):
    permission_classes = [HasFeaturePermission]
    required_permission = "aws:dashboard:view"
    def get(self, request): return Response({"service": "aws", "connectionCount": AwsConnection.objects.count()})


class AwsConnectionViewSet(viewsets.ModelViewSet):
    queryset = AwsConnection.objects.all()
    serializer_class = AwsConnectionSerializer
    permission_classes = [HasFeaturePermission]

    def get_required_permission(self):
        return {
            "list": "aws:connections:view", "retrieve": "aws:connections:view",
            "create": "aws:connections:create", "update": "aws:connections:update",
            "partial_update": "aws:connections:update", "destroy": "aws:connections:delete",
        }.get(self.action)

    @property
    def required_permission(self): return self.get_required_permission()

    def perform_create(self, serializer): serializer.save(created_by_user_id=self.request.user.id)

