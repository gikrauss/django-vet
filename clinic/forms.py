from django import forms
from .models import Client, Patient

class ClientForm(forms.ModelForm):
	class Meta:
		model = Client
		fields = ['firstname', 'lastname', 'email']

class PatientForm(forms.ModelForm):
	class Meta:
		model = Patient
		fields = ['name', 'specie', 'breed', 'gender', 'weight', 'birthday', 'identifier']