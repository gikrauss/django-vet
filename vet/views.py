from django.http import HttpResponse
from django.views.generic import TemplateView
from django.template import Template, Context

class IndexView(TemplateView):
	template_name = "index.html"

class MedicalRecordView(TemplateView):
	template_name = "clinic/medical-record.html"

class PatientsListView(TemplateView):
	template_name = "clinic/patients.html"

class ClientsListView(TemplateView):
	template_name = "clinic/clients.html"