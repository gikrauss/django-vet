from django.conf.urls import patterns, include, url
from django.contrib import admin
from vet.views import IndexView, MedicalRecordView

urlpatterns = patterns('',
    url(r'^chaining/', include('smart_selects.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/', IndexView.as_view(), name='home'),    
    url(r'^medical/', MedicalRecordView.as_view(), name='medical_record'),
    url(r'^patients/', 'vet.views.PatientsListView', name='patients_list'),
    url(r'^clients/', 'vet.views.ClientsListView', name='clients_list'), 
    url(r'^', include('clinic.urls', namespace='clinica')),
)
