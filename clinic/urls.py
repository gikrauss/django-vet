from django.conf.urls import patterns, include, url
from .views import MedicalRecordView, RegisterClient, RegisterPatient, ClientsList, EditClient, ClientDetails, DeleteClient, PatientsList, EditPatient, DeletePatient, PatientDetails

urlpatterns = patterns('',    
    url(r'^clinica/pacientes/$', PatientsList.as_view(), name='patients_list'),
    url(r'^clinica/patient/(?P<pk>\d+)/$', PatientDetails.as_view(), name='patient_details'),
    url(r'^clinica/patient/editar/(?P<pk>\d+)/$', EditPatient.as_view(), name='edit_patient'),
    url(r'^clinica/patient/borrar/(?P<pk>\d+)/$', DeletePatient.as_view(), name='delete_patient'),
    url(r'^clinica/pacientes/nuevo/', RegisterPatient.as_view(), name='register_patient'),
    url(r'^clinica/clientes/$', ClientsList.as_view(), name='clients_list'),
    url(r'^clinica/cliente/(?P<pk>\d+)/$', ClientDetails.as_view(), name='client_details'),
    url(r'^clinica/cliente/editar/(?P<pk>\d+)/$', EditClient.as_view(), name='edit_client'),
    url(r'^clinica/cliente/borrar/(?P<pk>\d+)/$', DeleteClient.as_view(), name='delete_client'),
    url(r'^clinica/clientes/nuevo/', RegisterClient.as_view(), name='register_client'),
    url(r'^clinica/medical/$', MedicalRecordView.as_view(), name='medicalrecord'),
    url(r'^clinica/conf/raza/$', 'clinic.views.BreedView', name='breed_conf'),
    url(r'^clinica/conf/especie/$', 'clinic.views.SpecieView', name='specie_conf'),
    url(r'^clinica/conf/genero/$', 'clinic.views.GenderView', name='gender_conf'),
)