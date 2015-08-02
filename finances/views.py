from django.core.urlresolvers import reverse_lazy
from vanilla import ListView, UpdateView, DetailView, DeleteView
from .models import Item, Provider, Sales

class ProviderList(ListView):
    model = Provider
    template_name = "finances/providers.html"

class EditProvider(UpdateView):
    model = Provider
    fields = ['name', 'phone', 'email']
    template_name = "finances/provider_edit.html"
    success_url = reverse_lazy('finances:provider_list')

class DeleteProvider(DeleteView):
    model = Provider
    success_url = reverse_lazy('finances:provider_list')