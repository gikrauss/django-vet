from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import TemplateView, CreateView
from django.core.urlresolvers import reverse_lazy
from .models import Client, Patient

class RegisterClient(CreateView):
	template_name = "clinic/register.html"
	model = Client
	success_url = reverse_lazy('clinic.register_client')

	def post(self, request, *args, **kwargs):
		client = Client()
		client.save()
		return render_to_response('clinic/register.html', context_instance=RequestContext(request))

class RegisterPatient(CreateView):
	template_name = "clinic/register.html"
	model = Patient
	success_url = reverse_lazy('clinic.register_patient')

	def post(self, request, *args, **kwargs):
		patient = Patient()
		patient.save()
		return render_to_response('clinic/register.html', context_instance=RequestContext(request))

def ClientsListView(request):
	template_name = "clinic/clients.html"
	title = "Clientes"	
	registro = "Cliente"
	client = Client.objects.all()
	context = {
		'queryset': client,
		'title': title,
		'reg': registro,
	}
	return render(request, 'clinic/clients.html', context)

def PatientsListView(request):
	template_name = "clinic/patients.html"
	title = "Pacientes"
	registro = "Paciente"
	patient = Patient.objects.all()
	context = {
		'queryset': patient,
		'title': title,		
		'reg': registro,
	}
	return render(request, 'clinic/patients.html', context)

class MedicalRecordView(TemplateView):
	template_name = "clinic/medical-record.html"