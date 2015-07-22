from django.conf.urls import patterns, include, url
from django.contrib import admin
from vet.views import IndexView, MedicalRecordView, PatientsListView, ClientsListView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'vet.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^chaining/', include('smart_selects.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/', IndexView.as_view(), name='home'),
    url(r'^medical/', MedicalRecordView.as_view(), name='medical_record'),
    url(r'^clients/', ClientsListView.as_view(), name='clients_list'),
    url(r'^patients/', PatientsListView.as_view(), name='patients_list'),
    url(r'^', include('clinic.urls', namespace='clinica')),
)
