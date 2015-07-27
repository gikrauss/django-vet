from django.shortcuts import render, render_to_response
from django.template import RequestContext, Context, Template
from django.views.generic import TemplateView, CreateView, ListView
from .models import Client, Patient, Breed, Gender, Specie
from .forms import BreedForm, SpecieForm, GenderForm

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
	patient = Patient.objects.all()
	context = {
		'queryset': patient,
		'title': title
	}
	return render(request, 'clinic/patients.html', context)

class MedicalRecordView(TemplateView):
	template_name = "clinic/medical-record.html"

def BreedView(request):
    if request.method == "POST":

        form = BreedForm(request.POST)

        if(form.is_valid()):
        	message = 'Guardado Exitoso'
        else:
            message = 'Error, complete los campos correctamente'

        return render_to_response('clinic/conf/register_breed.html',
              {'message': message, 'title': "Razas"},
              context_instance=RequestContext(request))
    else:
        return render_to_response('clinic/conf/register_breed.html',
                {'form': BreedForm(),
                'title': "Razas",
                },
                context_instance=RequestContext(request))

def SpecieView(request):
    if request.method == "POST":

        form = SpecieForm(request.POST)

        if(form.is_valid()):
            message = 'success'
        else:
            message = 'fail'

        return render_to_response('clinic/conf/register_specie.html',
              {'message': message},
              context_instance=RequestContext(request))
    else:
        return render_to_response('clinic/conf/register_specie.html',
                {'form': SpecieForm()},
                context_instance=RequestContext(request))

def GenderView(request):
    if request.method == "POST":

        form = GenderForm(request.POST)

        if(form.is_valid()):
            message = 'Guardado'
        else:
            message = 'fail'

        return render_to_response('clinic/conf/register_gender.html',
              {'message': message},
              context_instance=RequestContext(request))
    else:
        return render_to_response('clinic/conf/register_gender.html',
                {'form': GenderForm()},
                context_instance=RequestContext(request))