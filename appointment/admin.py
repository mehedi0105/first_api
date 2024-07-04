from django.contrib import admin
from .models import Appointment
# Register your models here.
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['doctor','patient']
    def doctor(self,obj):
        return obj.doctor.user.first_name
    def patient(self,obj):
        return obj.patient.user.first_name


admin.site.register(Appointment, AppointmentAdmin)