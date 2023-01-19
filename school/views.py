from rest_framework import viewsets, generics
from school.models import Course, Registration, Studant
from school.serializers import CourseSerializer, RegistrationSerializer, StudantSerializer, StudantPerCourseSerializers, CoursesPerStudantSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class CourseViewSet(viewsets.ModelViewSet):
    """Disponibiliza o CRUD para todos os Cursos"""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class RegistrationViewSet(viewsets.ModelViewSet):
    """Disponibiliza o CRUD para todas as Matrículas"""
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class StudantViewSet(viewsets.ModelViewSet):
    """Disponibiliza o CRUD para todos os Estudantes"""
    queryset = Studant.objects.all()
    serializer_class = StudantSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ListStudantsForCourse(generics.ListAPIView):
    """Exibe apenas os dados de um curso """
    def get_queryset(self):
        return Registration.objects.filter(course_id=self.kwargs['pk'])
    serializer_class = StudantPerCourseSerializers
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ListCoursePerStudant(generics.ListAPIView):
    """Lista todos os cursos em que um determinado aluno está matriculado"""
    def get_queryset(self):
        return Registration.objects.filter(studant_id=self.kwargs['pk'])
    serializer_class = CoursesPerStudantSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
