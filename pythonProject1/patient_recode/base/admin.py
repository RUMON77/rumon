from django.contrib import admin
from .models import Patient
# Register your models here.

class Patientadmin(admin.ModelAdmin):
    list_display=('name','mobile','detail', 'about', 'prescription' ,'visit_date','next_visit_date')
    search_fields=('full','mobile')

admin.site.register(Patient,Patientadmin)
