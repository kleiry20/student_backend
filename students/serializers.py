from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Student
        fields = ['id', 'studID', 'fname', 'lname', 'email']