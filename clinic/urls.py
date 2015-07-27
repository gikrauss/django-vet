from django.conf.urls import patterns, include, url
from .views import MedicalRecordView, RegisterClient, RegisterPatient

urlpatterns = patterns('',    
    url(r'^clinica/pacientes/$', 'clinic.views.PatientsListView', name='patients_list'),
    url(r'^clinica/pacientes/nuevo/', RegisterPatient.as_view(), name='register_patient'),
    url(r'^clinica/clientes/$', 'clinic.views.ClientsListView', name='clients_list'),
    url(r'^clinica/cliente/(?P<pk>\d+)/$', 'clinic.views.ClientDetailView', name='client_detail'),
    url(r'^clinica/clientes/nuevo/', RegisterClient.as_view(), name='register_client'),
    url(r'^clinica/medical/$', MedicalRecordView.as_view(), name='medicalrecord'),
    url(r'^clinica/conf/raza/$', 'clinic.views.BreedView', name='breed_conf'),
    url(r'^clinica/conf/especie/$', 'clinic.views.SpecieView', name='specie_conf'),
    url(r'^clinica/conf/genero/$', 'clinic.views.GenderView', name='gender_conf'),
)