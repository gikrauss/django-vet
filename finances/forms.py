from django import forms
from django.forms.models import inlineformset_factory, modelformset_factory
from .models import Item, Provider, Sales, Buy

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        exclude = []

class SalesForm(forms.ModelForm):
    class Meta:
        model = Sales
        exclude = []

class ProviderForm(forms.ModelForm):
    class Meta:
        model = Provider
        exclude = []

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Buy
        exclude = []
