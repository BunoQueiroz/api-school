from rest_framework import generics, viewsets
from registration.models import Registration
from registration.serializers import RegistrationSerializer
from course.serializers import CoursesPerStudantSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication

class RegistrationViewSet(viewsets.ModelViewSet):
    """Disponibiliza o CRUD para todas as Matrículas"""
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ListCoursePerStudant(generics.ListAPIView):
    """Lista todos os cursos em que um determinado aluno está matriculado"""
    def get_queryset(self):
        return Registration.objects.filter(studant_id=self.kwargs['pk'])
    serializer_class = CoursesPerStudantSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
