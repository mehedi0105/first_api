from django.shortcuts import render
from rest_framework import viewsets
from .models import Appointment
from .serialaizers import AppointmentSerializer
# Create your views here.
class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    # cust query set
    def get_queryset(self):
        queryset = super().get_queryset()
        print(self.request.query_params)
        patient_id =  self.request.query_params.get('patient_id')
        if patient_id:
            queryset = queryset.filter(patient_id= patient_id)
        return queryset