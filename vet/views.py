from django.http import HttpResponse
from django.views.generic import TemplateView
from django.template import Template, Context
from django.shortcuts import render
from clinic.models import Client, Patient

class IndexView(TemplateView):
	template_name = "index.html"

class MedicalRecordView(TemplateView):
	template_name = "clinic/medical-record.html"

class PatientsListView(TemplateView):
	template_name = "clinic/patients.html"

def ClientsListView(request):
	template_name = "clinic/clients.html"
	title = "Clientes"	
	reg = "Cliente"
	client = Client.objects.all()
	context = {
		'queryset': client,
		'title': title,
		'reg': reg
	}
	return render(request, 'clinic/clients.html', context)

def PatientsListView(request):
	template_name = "clinic/patients.html"
	title = "Pacientes"
	reg = "Paciente"
	patient = Patient.objects.all()
	context = {
		'queryset': patient,
		'title': title,		
		'reg': reg
	}
	return render(request, 'clinic/patients.html', context)
		

