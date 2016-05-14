from django import forms
from django.forms.models import inlineformset_factory, modelformset_factory
from .models import Client, Address, PhoneNumber, Patient, MedicalRecord, Vaccine, Complementary, Deworming, Analysis
from localflavor.ar import ar_provinces

class ClientForm(forms.ModelForm):
  class Meta:
    model = Client
    exclude = []

AddressInlineFormSet = inlineformset_factory(Client, Address, extra=1, exclude=(),)
PhoneInlineFormSet = inlineformset_factory(Client, PhoneNumber, extra=1, exclude=(),)

class PatientForm(forms.ModelForm):
  class Meta:
    model = Patient
    exclude = []
    widgets = {
    'initial_anamnesis': forms.Textarea(attrs={'rows':3}),
    }

  def __init__(self, *args, **kwargs):
    owner = kwargs.pop('owner', None)
    super(PatientForm, self).__init__(*args, **kwargs)
    if owner:
        self.instance.owner = owner

class MedicalRecordForm(forms.ModelForm):
  class Meta:
    model = MedicalRecord
    fields = ['date', 'motive', 'temp', 'fc', 'fr', 'tllc', 'anamnesis', 'exam', 'diagnostic', 'tto', 'attached']
    widgets = {
    'motive': forms.Textarea(attrs={'rows':2}),
    'anamnesis': forms.Textarea(attrs={'rows':3}),
    'exam': forms.Textarea(attrs={'rows':3}),
    'diagnostic': forms.Textarea(attrs={'rows':3}),
    'tto': forms.Textarea(attrs={'rows':3}),
    }

  def __init__(self, *args, **kwargs):
    patient = kwargs.pop('patient', None)
    super(MedicalRecordForm, self).__init__(*args, **kwargs)
    if patient:
        self.instance.patient = patient

class VaccineForm(forms.ModelForm):
  class Meta:
    model = Vaccine
    fields = ['vac_type', 'marca', 'date', 'expire_date', 'next_vac']

  def __init__(self, *args, **kwargs):
    patient = kwargs.pop('patient', None)
    super(VaccineForm, self).__init__(*args, **kwargs)
    if patient:
        self.instance.patient = patient

class ComplementaryForm(forms.ModelForm):
  class Meta:
    model = Complementary
    fields = ['name', 'date', 'description', 'attached']

  def __init__(self, *args, **kwargs):
    patient = kwargs.pop('patient', None)
    super(ComplementaryForm, self).__init__(*args, **kwargs)
    if patient:
        self.instance.patient = patient

class DewormingForm(forms.ModelForm):
  class Meta:
    model = Deworming
    fields = ['date', 'name', 'dose']

  def __init__(self, *args, **kwargs):
    patient = kwargs.pop('patient', None)
    super(DewormingForm, self).__init__(*args, **kwargs)
    if patient:
        self.instance.patient = patient

class AnalysisForm(forms.ModelForm):
  class Meta:
    model = Analysis
    exclude = []
