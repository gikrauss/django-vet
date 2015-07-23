from django.http import HttpResponse
from django.views.generic import TemplateView
from django.template import Template, Context
from django.shortcuts import render
from clinic.models import Client, Patient

class IndexView(TemplateView):
	template_name = "index.html"


