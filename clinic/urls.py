from django.conf.urls import patterns, include, url
from .views import RegisterClient, RegisterPatient

urlpatterns = patterns('',       
    url(r'^clinic/client_reg/', RegisterClient.as_view(), name='register_client'),
    url(r'^clinic/patient_reg/', RegisterPatient.as_view(), name='register_patient'),
)