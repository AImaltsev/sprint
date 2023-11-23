from rest_framework import serializers
from .models import PerevalAdded


class PerevalSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerevalAdded
        fields = '__all__'