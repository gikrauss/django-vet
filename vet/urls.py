from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import IndexView, RegisterClient, RegisterPatient
from clinic.views import MedicalRecordView

urlpatterns = patterns('',
    url(r'^chaining/', include('smart_selects.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/', IndexView.as_view(), name='home'),
    url(r'^', include('clinic.urls', namespace='clinic')),
    url(r'^clinica/pacientes/$', 'clinic.views.PatientsListView', name='patients_list'),
    url(r'^clinica/pacientes/nuevo/', RegisterPatient.as_view(), name='register_patient'),
    url(r'^clinica/clientes/$', 'clinic.views.ClientsListView', name='clients_list'),
    url(r'^clinica/clientes/nuevo/', RegisterClient.as_view(), name='register_client'),
    url(r'^clinica/medical/$', MedicalRecordView.as_view(), name='medical_record'),  
)
