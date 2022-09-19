from rest_framework import serializers
from .models import StudentClassMap


class StudentClassMapSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    standard_name = serializers.CharField(source='stdID.stdName', read_only=True)

    class Meta:
        model = StudentClassMap
        fields = ['id', 'stdID', 'studID','standard_name', 'marks', 'rank']   