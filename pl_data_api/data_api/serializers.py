from django.db import IntegrityError
from rest_framework import serializers

from .models import OperationalParametersModel


class OperationalParametersSerializer(serializers.ModelSerializer):
    class Meta:
        model = OperationalParametersModel
        fields = "__all__"

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            print(f"Ignoring not unique value - {validated_data}")