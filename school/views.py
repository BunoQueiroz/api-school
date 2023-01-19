from rest_framework import viewsets, generics
from school.models import Course, Registration, Studant
from school.serializers import CourseSerializer, RegistrationSerializer, StudantSerializer, StudantForCourseSerializers

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

class ListStudantsForCourse(generics.ListAPIView):
    """Exibe apenas os dados de um curso """
    def get_queryset(self):
        return Registration.objects.filter(course_id=self.kwargs['pk'])
    serializer_class = StudantForCourseSerializers
