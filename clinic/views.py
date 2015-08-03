from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext, Context, Template
from .models import Client, Address, PhoneNumber, Patient, Breed, Specie, Vac_Type
from .forms import BreedForm, SpecieForm, Vac_TypeForm, ClientForm, AddressInlineFormSet, PhoneInlineFormSet, PatientForm, MedicalRecordForm, VaccineForm, ComplementaryForm
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

def AddPatient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            patient = form.save()
            return redirect('clinic:patients_list')
    else:
        form = PatientForm()
    return render_to_response('clinic/register_patient.html', {'form': form}, context_instance=RequestContext(request))

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

def AddMedicalRecord(request):
    if request.method == 'POST':
        form1 = MedicalRecordForm(request.POST)
        form2 = VaccineForm(request.POST)
        form3 = ComplementaryForm(request.POST)
        if form1.is_valid():
            medical_record = form1.save()
            return redirect('clinic:patient_detail')
        if form2.is_valid():
            medical_record = form2.save()
            return redirect('clinic:patient_detail')
        if form3.is_valid():
            medical_record = form3.save()
            return redirect('clinic:patient_detail')
    else:
        form1 = MedicalRecordForm()
        form2 = VaccineForm()
        form3 = ComplementaryForm()
    return render_to_response('clinic/register_medicalrecord.html', {'form_consult': form1, 'form_vac': form2, 'form_complementary': form3}, context_instance=RequestContext(request))

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
