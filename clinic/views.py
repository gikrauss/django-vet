from django.shortcuts import render, render_to_response
from django.template import RequestContext, Context, Template
from django.views.generic import TemplateView, CreateView
from .models import Client, Patient, Breed, Gender, Specie
from .forms import BreedForm, SpecieForm, GenderForm
from django.core.urlresolvers import reverse_lazy
from vanilla import ListView, UpdateView, DetailView, DeleteView

class ClientsList(ListView):
    model = Client
    template_name = "clinic/clients.html"

class EditClient(UpdateView):
    model = Client
    fields = ['lastname', 'firstname', 'email']
    template_name = "clinic/client_edit.html"
    success_url = reverse_lazy('clinic:clients_list')

class ClientDetails(DetailView):
    model = Client

class DeleteClient(DeleteView):
    model = Client
    success_url = reverse_lazy('clinic:clients_list')


class PatientsList(ListView):
    model = Patient
    template_name = "clinic/patients.html"

class PatientDetails(DetailView):
    model = Patient

class EditPatient(UpdateView):
    model = Patient
    fields = ['name', 'owner', 'specie', 'breed', 'gender', 'birthday', 'weight', 'identifier']
    template_name = "clinic/patient_edit.html"
    success_url = reverse_lazy('clinic:patients_list')

class DeletePatient(DeleteView):
    model = Patient
    success_url = reverse_lazy('clinic:patients_list')

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