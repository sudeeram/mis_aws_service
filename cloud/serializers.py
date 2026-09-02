from rest_framework import serializers
from .models import AwsConnection


class AwsConnectionSerializer(serializers.ModelSerializer):
    def validate_aws_account_id(self, value):
        if len(value) != 12 or not value.isdigit():
            raise serializers.ValidationError("AWS account ID must contain exactly 12 digits.")
        return value

    class Meta:
        model = AwsConnection
        fields = ("id", "name", "aws_account_id", "default_region", "authentication_method", "status", "created_by_user_id", "created_at", "updated_at")
        read_only_fields = ("id", "created_by_user_id", "created_at", "updated_at")

