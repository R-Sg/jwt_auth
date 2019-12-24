from jwtfire.models import *
from rest_framework import serializers


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'name',
            'email',
            'password',
        )
        model = Student
