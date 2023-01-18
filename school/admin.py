from django.contrib import admin
from school.models import Course, Registration, Studant

class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'level', 'duration', 'category']
    list_display_links = ['id',]
    search_fields = ['description',]
    list_editable = ['duration',]
    list_filter = ['category',]
    list_per_page = 20

class RegistrationAdmin(admin.ModelAdmin):
    list_display = ['id', 'studant', 'course', 'initial_date', 'deadline']
    list_display_links = ['id',]
    search_fields = ['studant',]
    list_editable = ['deadline',]
    list_filter = ['course',]
    list_per_page = 20

class StudantAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'rg', 'cpf', 'email']
    list_display_links = ['id',]
    search_fields = ['first_name', 'last_name']
    list_editable = ['first_name', 'last_name']
    list_per_page = 20

admin.site.register(Course, CourseAdmin)
admin.site.register(Registration, RegistrationAdmin)
admin.site.register(Studant, StudantAdmin)
