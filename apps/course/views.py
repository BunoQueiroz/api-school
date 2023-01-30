from course.models import Course
from course.serializers import CourseSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

class CourseViewSet(viewsets.ModelViewSet):
    """Disponibiliza o CRUD para todos os Cursos"""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
