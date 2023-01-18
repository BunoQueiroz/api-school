from rest_framework import viewsets
from school.models import Course, Registration, Studant
from school.serializers import CourseSerializer, RegistrationSerializer, StudantSerializer

class CourseViewSet(viewsets.ModelViewSet):
    """Disponibiliza o CRUD para todos os Cursos"""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class RegistrationViewSet(viewsets.ModelViewSet):
    """Disponibiliza o CRUD para todas as Matrículas"""
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer

class StudantViewSet(viewsets.ModelViewSet):
    """Disponibiliza o CRUD para todos os Estudantes"""
    queryset = Studant.objects.all()
    serializer_class = StudantSerializer
