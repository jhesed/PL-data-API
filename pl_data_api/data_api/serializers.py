from rest_framework import serializers
from .models import OperationalParametersModel


class OperationalParametersSerializer(serializers.ModelSerializer):
    class Meta:
        model = OperationalParametersModel
        fields = "__all__"
