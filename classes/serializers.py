from rest_framework import serializers
from .models import Standard

class StandardSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Standard
        fields = ['id', 'stdID', 'stdName']        