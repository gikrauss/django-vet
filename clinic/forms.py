from django import forms
from django.forms.models import inlineformset_factory
from .models import Breed, Specie, Vac_Type, Client, Address, PhoneNumber, Patient, MedicalRecord, Vaccine, Complementary
from localflavor.ar import ar_provinces  

class BreedForm(forms.ModelForm):
  class Meta:
    model = Breed
    fields = ('name', 'specie')

class SpecieForm(forms.ModelForm):
    class Meta:
     model = Specie

class Vac_TypeForm(forms.ModelForm):
  class Meta:
    model = Vac_Type

class ClientForm(forms.ModelForm):
  class Meta:
    model = Client

AddressInlineFormSet = inlineformset_factory(Client, Address, extra=1)
PhoneInlineFormSet = inlineformset_factory(Client, PhoneNumber, extra=1)

class PatientForm(forms.ModelForm):
  class Meta:
    model = Patient

class MedicalRecordForm(forms.ModelForm):
  class Meta:
    model = MedicalRecord

class VaccineForm(forms.ModelForm):
  class Meta:
    model = Vaccine

class ComplementaryForm(forms.ModelForm):
  class Meta:
    model = Complementary