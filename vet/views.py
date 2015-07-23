from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.generic import TemplateView, CreateView
from django.core.urlresolvers import reverse_lazy
from django.template import Template, Context, RequestContext
from clinic.models import Client, Patient

class IndexView(TemplateView):
	template_name = "index.html"

class RegisterClient(CreateView):
	template_name = "clinic/register.html"
	model = Client
	success_url = reverse_lazy('register_client')

	def post(self, request, *args, **kwargs):
		client = Client()
		client.save()
		return render_to_response('clinic/clients.html', context_instance=RequestContext(request))

class RegisterPatient(CreateView):
	template_name = "clinic/register.html"
	model = Patient
	success_url = reverse_lazy('register_patient')

	def post(self, request, *args, **kwargs):
		patient = Patient()
		patient.save()
		return render_to_response('clinic/patients.html', context_instance=RequestContext(request))


