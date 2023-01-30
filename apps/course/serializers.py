from rest_framework import serializers
from course.models import Course
from registration.models import Registration

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

class CoursesPerStudantSerializer(serializers.ModelSerializer):
    initial_date = serializers.DateField(format='%d-%m-%Y')
    deadline = serializers.DateField(format='%d-%m-%Y')
    course = serializers.ReadOnlyField(source='course.description')
    class Meta:
        model = Registration
        exclude = ['studant', ]
