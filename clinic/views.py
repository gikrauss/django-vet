from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.generic import TemplateView
from .models import Client, Patient

def ClientsListView(request):
	template_name = "clinic/clients.html"
	title = "Clientes"
	client = Client.objects.all()
	context = {
		'queryset': client,
		'title': title
	}
	return render(request, 'clinic/clients.html', context)

def PatientsListView(request):
	template_name = "clinic/patients.html"
	title = "Pacientes"
	registro = "Paciente"
	patient = Patient.objects.all()
	context = {
		'queryset': patient,
		'title': title
	}
	return render(request, 'clinic/patients.html', context)

class MedicalRecordView(TemplateView):
	template_name = "clinic/medical-record.html"