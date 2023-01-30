from rest_framework import serializers
from registration.models import Registration

class RegistrationSerializer(serializers.ModelSerializer):
    studant = serializers.ReadOnlyField(source='studant.first_name')
    course = serializers.ReadOnlyField(source='course.description')
    initial_date = serializers.DateField(format='%d-%m-%Y')
    deadline = serializers.DateField(format='%d-%m-%Y')
    class Meta:
        model = Registration
        fields = ['id', 'studant', 'course', 'initial_date', 'deadline']
