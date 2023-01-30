from rest_framework import serializers
from registration.models import Registration
from studant.models import Studant

class StudantSerializer(serializers.ModelSerializer):
    date_birth = serializers.DateField(format='%d-%m-%Y')
    class Meta:
        model = Studant
        fields = '__all__'

class StudantPerCourseSerializers(serializers.ModelSerializer):
    studant = serializers.ReadOnlyField(source='studant.first_name')
    initial_date = serializers.DateField(format='%d-%m-%Y')
    deadline = serializers.DateField(format='%d-%m-%Y')
    class Meta:
        model = Registration
        exclude = ['course', ]

