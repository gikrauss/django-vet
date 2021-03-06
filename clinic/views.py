from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponsePermanentRedirect
from django.template import RequestContext, Context, Template
from .models import Client, Address, PhoneNumber, Patient, Vaccine
from .forms import ClientForm, AddressInlineFormSet, PhoneInlineFormSet, PatientForm, MedicalRecordForm, VaccineForm, DewormingForm, ComplementaryForm, AnalysisForm
from django.core.urlresolvers import reverse_lazy, reverse
from vanilla import ListView, UpdateView, DetailView, DeleteView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def clients_list(request):
    list = Client.objects.all()
    paginator = Paginator(list, 15) # Show 15 contacts per page
    page = request.GET.get('page')
    try:
        clients = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        clients = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        clients = paginator.page(paginator.num_pages)
    return render_to_response('clinic/client_list.html', {'list': clients, 'paginator': paginator})

def add_client(request):
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

def patients_list(request):
    list = Patient.objects.all()
    paginator = Paginator(list, 15)
    page = request.GET.get('page')
    try:
        patients = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        patients = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        patients = paginator.page(paginator.num_pages)
    return render_to_response('clinic/patient_list.html', {'list': patients, 'paginator': paginator})

def add_patient(request, pk):
    if request.method == 'POST':
        form = PatientForm(request.POST, owner=Client.objects.get(pk=pk))
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
    fields = ['name', 'owner', 'specie', 'breed', 'gender', 'neutered', 'birthday', 'weight', 'identifier']
    template_name = "clinic/patient_edit.html"
    success_url = reverse_lazy('clinic:patients_list')

class DeletePatient(DeleteView):
    model = Patient
    success_url = reverse_lazy('clinic:patients_list')

def add_consult(request, pk):
    if request.method == 'POST':
        form = MedicalRecordForm(request.POST, patient=Patient.objects.get(pk=pk))
        if form.is_valid():
            medicalrecord = form.save()
            patient=Patient.objects.get(pk=pk)
            return redirect('/clinica/pacientes/')
    else:
        form = MedicalRecordForm()
    return render_to_response('clinic/medicalrecord/register_consult.html', {'form': form}, context_instance=RequestContext(request))

def add_vaccine(request, pk):
    if request.method == 'POST':
        form = VaccineForm(request.POST, patient=Patient.objects.get(pk=pk))
        if form.is_valid():
            vaccine = form.save()
            patient=Patient.objects.get(pk=pk)
            return redirect('clinic:patient_detail', patient.pk)
    else:
        form = VaccineForm()
    return render_to_response('clinic/medicalrecord/register_vaccine.html', {'form_vaccine': form}, context_instance=RequestContext(request))

def add_deworming(request, pk):
    if request.method == 'POST':
        form = DewormingForm(request.POST, patient=Patient.objects.get(pk=pk))
        if form.is_valid():
            deworming = form.save()
            patient=Patient.objects.get(pk=pk)
            return redirect('clinic:patient_detail', patient.pk)
    else:
        form = DewormingForm()
    return render_to_response('clinic/medicalrecord/register_deworming.html', {'form_deworming': form}, context_instance=RequestContext(request))

def add_complementary(request, pk):
    if request.method == 'POST':
        form = ComplementaryForm(request.POST, patient=Patient.objects.get(pk=pk))
        if form.is_valid():
            complementary = form.save()
            patient=Patient.objects.get(pk=pk)
            return redirect('clinic:patient_detail', patient.pk)
    else:
        form = ComplementaryForm()
    return render_to_response('clinic/medicalrecord/register_complementary.html', {'form_complementary': form}, context_instance=RequestContext(request))

