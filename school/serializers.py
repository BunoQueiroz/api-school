from rest_framework import serializers
from .models import Studant, Course, Registration

class StudantSerializer(serializers.ModelSerializer):
    date_birth = serializers.DateField(format='%d-%m-%Y')
    class Meta:
        model = Studant
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    level = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()
    class Meta:
        model = Course
        exclude = ['id']

    def get_level(self, obj):
        return obj.get_level_display()

    def get_category(self, obj):
        return obj.get_category_display()

class RegistrationSerializer(serializers.ModelSerializer):
    studant = serializers.ReadOnlyField(source='studant.first_name')
    course = serializers.ReadOnlyField(source='course.description')
    initial_date = serializers.DateField(format='%d-%m-%Y')
    deadline = serializers.DateField(format='%d-%m-%Y')
    class Meta:
        model = Registration
        fields = ['id', 'studant', 'course', 'initial_date', 'deadline']

class StudantPerCourseSerializers(serializers.ModelSerializer):
    studant = serializers.ReadOnlyField(source='studant.first_name')
    initial_date = serializers.DateField(format='%d-%m-%Y')
    deadline = serializers.DateField(format='%d-%m-%Y')
    class Meta:
        model = Registration
        exclude = ['course', ]
