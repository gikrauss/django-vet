from django import forms
from django.forms import ModelForm
from .models import Specie, Gender, Breed

class BreedForm(ModelForm):
    class Meta:
        model = Breed

class SpecieForm(ModelForm):
    class Meta:
        model = Specie

class GenderForm(ModelForm):
    class Meta:
        model = Gender