from django.shortcuts import render, render_to_response
from django.core.urlresolvers import reverse_lazy
from vanilla import ListView, UpdateView, DeleteView
from .models import *
from django.template import RequestContext, Context, Template
from .forms import BreedForm, SpecieForm, Vac_TypeForm

class BreedList(ListView):
    model = Breed
    template_name = 'settings/razas.html'

def add_breed(request):
    if request.method == "POST":
        form = BreedForm(request.POST)
        if(form.is_valid()):
            message = 'Registro de Raza Exitoso'
            form.save()
        else:
            message = 'Error en Registro'
        return render_to_response('settings/register.html',
              {'message': message, 'title': 'Registro nueva Raza'},
              context_instance=RequestContext(request))
    else:
        form = BreedForm()
    return render_to_response('settings/register.html', {'form': form, 'title': 'Registro nueva Raza'},
                context_instance=RequestContext(request))

class EditBreed(UpdateView):
    model = Breed
    fields = ['name','specie']
    template_name = "settings/conf_edit.html"
    success_url = reverse_lazy('settings:breed_conf')

class DeleteBreed(DeleteView):
    model = Breed
    success_url = reverse_lazy('settings:breed_conf')

class SpecieList(ListView):
    model = Specie
    template_name = 'settings/especies.html'

def add_specie(request):
    if request.method == "POST":
        form = SpecieForm(request.POST)
        if(form.is_valid()):
            message = 'Registro de Especie Exitoso'
            form.save()
        else:
            message = 'Error en el Registro'
        return render_to_response('settings/register.html',
              {'message': message, 'title': 'Registro nueva Especie'},
              context_instance=RequestContext(request))
    else:
        form = SpecieForm()
    return render_to_response('settings/register.html', {'form': form, 'title': 'Registro nueva Especie'},
                context_instance=RequestContext(request))

class EditSpecie(UpdateView):
    model = Specie
    fields = ['name']
    template_name = "settings/conf_edit.html"
    success_url = reverse_lazy('settings:specie_conf')

class DeleteSpecie(DeleteView):
    model = Specie
    success_url = reverse_lazy('settings:specie_conf')

class Vac_TypeList(ListView):
    model = Vac_Type
    template_name = 'settings/vacunas.html'

def add_vac_type(request):
    if request.method == "POST":

        form = Vac_TypeForm(request.POST)

        if(form.is_valid()):
            message = 'Registro de Vacuna Exitoso'
            form.save()
        else:
            message = 'Error'

        return render_to_response('settings/register.html',
              {'message': message, 'title': 'Registro nueva vacuna'},
              context_instance=RequestContext(request))
    else:
        return render_to_response('settings/register.html', {'form': Vac_TypeForm(), 'title': 'Registro nueva vacuna'},
                context_instance=RequestContext(request))

class EditVac_Type(UpdateView):
    model = Vac_Type
    fields = ['name', 'description']
    template_name = "settings/conf_edit.html"
    success_url = reverse_lazy('settings:vac_conf')

class DeleteVac_Type(DeleteView):
    model = Vac_Type
    success_url = reverse_lazy('settings:vac_conf')

