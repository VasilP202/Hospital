from django.contrib import admin

from .models import Department, Hospitalization, Examination, Medicine, Dose

admin.site.register(Department)
admin.site.register(Hospitalization)
admin.site.register(Examination)
admin.site.register(Medicine)
admin.site.register(Dose)
