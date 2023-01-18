from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from school.views import CourseViewSet, StudantViewSet, RegistrationViewSet

router = routers.DefaultRouter()
router.register('studants', StudantViewSet, 'studants')
router.register('courses', CourseViewSet, 'courses')
router.register('registrations', RegistrationViewSet, 'registrations')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
