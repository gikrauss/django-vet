from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext, Context, Template
from django.views.generic import TemplateView, CreateView
from .models import Client, Address, PhoneNumber, Patient, Breed, Specie, Vac_Type
from .forms import BreedForm, SpecieForm, Vac_TypeForm, ClientForm, AddressInlineFormSet, PhoneInlineFormSet
from django.core.urlresolvers import reverse_lazy
from vanilla import ListView, UpdateView, DetailView, DeleteView

class ClientsList(ListView):
    model = Client
    template_name = "clinic/clients.html"

def AddClient(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save()
            formset_address = AddressInlineFormSet(request.POST, instance=client)
            if formset_address.is_valid():
                formset_address.save()
                formset_phone = PhoneInlineFormSet(request.POST, instance=client)
                if formset_phone.is_valid():
                    formset_phone.save()
                    return redirect('clinic:clients_list')
            else:
                formset_phone = PhoneInlineFormSet(request.POST)
        else:
            formset_address = AddressInlineFormSet(request.POST)
    else:
        form = ClientForm()
        formset_address = AddressInlineFormSet()
        formset_phone = PhoneInlineFormSet()
    return render_to_response('clinic/register_client.html', {'form': form, 'formset_address': formset_address, 'formset_phone': formset_phone}, context_instance=RequestContext(request))

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

class BreedList(ListView):
    model = Breed
    template_name = 'clinic/conf/conf_list.html'

def BreedAdd(request):
    if request.method == "POST":

        form = BreedForm(request.POST)

        if(form.is_valid()):
            message = 'Registro de Raza Exitoso'
            form.save()
        else:
            message = 'Error'

        return render_to_response('clinic/conf/register.html',
              {'message': message},
              context_instance=RequestContext(request))
    else:
        return render_to_response('clinic/conf/register.html',
                {'form': SpecieForm(),
                'var': 'Raza'},
                context_instance=RequestContext(request))

class SpecieList(ListView):
    model = Specie
    template_name = 'clinic/conf/conf_list.html'

def SpecieAdd(request):
    if request.method == "POST":

        form = SpecieForm(request.POST)

        if(form.is_valid()):
            message = 'Registro de Especie Exitoso'
            form.save()
        else:
            message = 'Error'

        return render_to_response('clinic/conf/register.html',
              {'message': message},
              context_instance=RequestContext(request))
    else:
        return render_to_response('clinic/conf/register.html',
                {'form': SpecieForm(),
                'var': 'Especie'},
                context_instance=RequestContext(request))

class Vac_TypeList(ListView):
    model = Vac_Type
    template_name = 'clinic/conf/conf_list.html'

def Vac_TypeAdd(request):
    if request.method == "POST":

        form = Vac_TypeForm(request.POST)

        if(form.is_valid()):
            message = 'Registro de Vacuna Exitoso'
            form.save()
        else:
            message = 'Error'

        return render_to_response('clinic/conf/register.html',
              {'message': message},
              context_instance=RequestContext(request))
    else:
        return render_to_response('clinic/conf/register.html',
                {'form': Vac_TypeForm(),
                'var': 'Vacuna'},
                context_instance=RequestContext(request))

class RegisterPatient(CreateView):
    template_name = "clinic/register.html"
    model = Patient
    success_url = reverse_lazy('register_patient')

    def post(self, request, *args, **kwargs):
        patient = Patient()
        patient.save()
        return render_to_response('clinic/patients.html', context_instance=RequestContext(request))