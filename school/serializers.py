from rest_framework import serializers
from .models import Studant, Course, Registration

class StudantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Studant
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        exclude = ['id']

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = ['id', 'studant', 'course', 'initial_date', 'deadline']
