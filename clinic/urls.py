from django.conf.urls import patterns, include, url
from .views import RegisterPatient, ClientsList, EditClient, ClientDetails, DeleteClient, PatientsList, EditPatient, DeletePatient, PatientDetails, BreedList, SpecieList, Vac_TypeList

urlpatterns = patterns('',    
    url(r'^clinica/pacientes/$', PatientsList.as_view(), name='patients_list'),
    url(r'^clinica/paciente/(?P<pk>\d+)/$', PatientDetails.as_view(), name='patient_details'),
    url(r'^clinica/paciente/editar/(?P<pk>\d+)/$', EditPatient.as_view(), name='edit_patient'),
    url(r'^clinica/paciente/borrar/(?P<pk>\d+)/$', DeletePatient.as_view(), name='delete_patient'),
    url(r'^clinica/pacientes/nuevo/', RegisterPatient.as_view(), name='register_patient'),
    url(r'^clinica/clientes/$', ClientsList.as_view(), name='clients_list'),
    url(r'^clinica/cliente/(?P<pk>\d+)/$', ClientDetails.as_view(), name='client_details'),
    url(r'^clinica/cliente/editar/(?P<pk>\d+)/$', EditClient.as_view(), name='edit_client'),
    url(r'^clinica/cliente/borrar/(?P<pk>\d+)/$', DeleteClient.as_view(), name='delete_client'),
    url(r'^clinica/clientes/nuevo/', 'clinic.views.AddClient', name='register_client'),
    url(r'^clinica/conf/raza/$', BreedList.as_view(), name='breed_conf'),
    url(r'^clinica/conf/raza/nuevo/', 'clinic.views.BreedAdd', name='breed_conf_add'),
    url(r'^clinica/conf/especie/$', SpecieList.as_view(), name='specie_conf'),
    url(r'^clinica/conf/especie/nuevo/', 'clinic.views.SpecieAdd', name='specie_conf_add'),
    url(r'^clinica/conf/tipo_vac/$', Vac_TypeList.as_view(), name='vac_conf'),
    url(r'^clinica/conf/tipo_vac/nuevo/', 'clinic.views.Vac_TypeAdd', name='vac_conf_add'),
)