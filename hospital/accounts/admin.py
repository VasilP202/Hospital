from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Doctor, Pacient


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name',
                    'email', 'is_pacient', 'is_doctor')


class PacientProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_of_birth', 'residence', 'health_insurance')


class DoctorProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone')


admin.site.register(User, UserProfileAdmin)
admin.site.register(Doctor, DoctorProfileAdmin)
admin.site.register(Pacient, PacientProfileAdmin)
