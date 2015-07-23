from django.conf.urls import patterns, include, url
from .views import RegisterClient, RegisterPatient, MedicalRecordView


urlpatterns = patterns('',    
    url(r'^clinica/pacientes/', 'clinic.views.PatientsListView', name='patients_list'),
    url(r'^clinica/pacientes/nuevo', RegisterPatient.as_view(), name='register_patient'),
    url(r'^clinica/clientes/', 'clinic.views.ClientsListView', name='clients_list'),
    url(r'^clinica/clientes/nuevo', RegisterClient.as_view(), name='register_client'),
    url(r'^clinica/medical/', MedicalRecordView.as_view(), name='medical_record'),     
)