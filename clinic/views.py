from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import TemplateView, FormView, CreateView
from django.core.urlresolvers import reverse_lazy
from .models import Client, Patient

class RegisterClient(CreateView):
	template_name = "clinic/register.html"
	model = Client
	success_url = reverse_lazy('register_client')

	def post(self, request, *args, **kwargs):
		client = Client()
		client.save()
		return render_to_response('clinic/register.html', context_instance=RequestContext(request))

class RegisterPatient(CreateView):
	template_name = "clinic/register.html"
	model = Patient
	success_url = reverse_lazy('register_patient')

	def post(self, request, *args, **kwargs):
		patient = Patient()
		patient.save()
		return render_to_response('clinic/register.html', context_instance=RequestContext(request))