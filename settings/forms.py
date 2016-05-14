from django import forms
from .models import Breed, Specie, Vac_Type

class BreedForm(forms.ModelForm):
  class Meta:
    model = Breed
    fields = ('name', 'specie')

class SpecieForm(forms.ModelForm):
    class Meta:
     model = Specie
     exclude = []

class Vac_TypeForm(forms.ModelForm):
  class Meta:
    model = Vac_Type
    exclude = []