from rest_framework import serializers
from .models import StudentClassMap

class StudentClassMapSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = StudentClassMap
        fields = ['id', 'stdID', 'studID', 'marks', 'rank']   