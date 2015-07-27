from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.generic import TemplateView, CreateView
from django.template import Template, Context, RequestContext
from clinic.models import Client, Patient, Breed, Specie, Gender

class IndexView(TemplateView):
	template_name = "index.html"


