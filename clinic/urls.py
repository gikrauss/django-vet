from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',
    url(r'^pacientes/$', 'clinic.views.patients_list', name='patients_list'),
    url(r'^paciente/(?P<pk>\d+)/$', PatientDetails.as_view(), name='patient_details'),
    url(r'^paciente/(?P<pk>\d+)/consulta/$', 'clinic.views.add_consult', name='register_consult'),
    url(r'^paciente/(?P<pk>\d+)/vacuna/$', 'clinic.views.add_vaccine', name='register_vaccine'),
    url(r'^paciente/(?P<pk>\d+)/desparasitacion/$', 'clinic.views.add_deworming', name='register_deworming'),
    url(r'^paciente/(?P<pk>\d+)/complementarios/$', 'clinic.views.add_complementary', name='register_complementary'),
    url(r'^paciente/editar/(?P<pk>\d+)/$', EditPatient.as_view(), name='edit_patient'),
    url(r'^paciente/borrar/(?P<pk>\d+)/$', DeletePatient.as_view(), name='delete_patient'),
    url(r'^cliente/(?P<pk>\d+)/paciente/nuevo/', 'clinic.views.add_patient', name='register_patient'),
    url(r'^clientes/$', 'clinic.views.clients_list', name='clients_list'),
    url(r'^cliente/(?P<pk>\d+)/$', ClientDetails.as_view(), name='client_details'),
    url(r'^cliente/editar/(?P<pk>\d+)/$', EditClient.as_view(), name='edit_client'),
    url(r'^cliente/borrar/(?P<pk>\d+)/$', DeleteClient.as_view(), name='delete_client'),
    url(r'^clientes/nuevo/', 'clinic.views.add_client', name='register_client'),
)
