from rest_framework import generics
from registration.models import Registration
from studant.serializers import StudantPerCourseSerializers
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from studant.models import Studant
from studant.serializers import StudantSerializer

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
