from django.shortcuts import render, render_to_response, redirect
from django.core.urlresolvers import reverse_lazy
from django.template import RequestContext, Context, Template
from vanilla import ListView, UpdateView, DetailView, DeleteView
from .models import Item, Provider, Sales
from .forms import SalesForm, ItemForm, ProviderForm, PurchaseForm

class ProviderList(ListView):
    model = Provider
    template_name = "finances/provider_list.html"

def add_provider(request):
    title = "Proveedor"
    if request.method == 'POST':
        form = ProviderForm(request.POST)
        if form.is_valid():
            item = form.save()
            return redirect('finances:provider_list')          
    else:
        form = ProviderForm()
    return render_to_response('finances/register.html', {'form': form, 'title': title}, context_instance=RequestContext(request))

class EditProvider(UpdateView):
    model = Provider
    fields = ['name', 'phone', 'email']
    template_name = "finances/provider_edit.html"
    success_url = reverse_lazy('finances:provider_list')

class ProviderDetails(DetailView):
    model = Provider

class DeleteProvider(DeleteView):
    model = Provider
    success_url = reverse_lazy('finances:provider_list')

class ItemList(ListView):
    model = Item
    template_name = "finances/item_list.html"

def add_item(request):
    title = "Producto"
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save()
            return redirect('finances:item_list')          
    else:
        form = ItemForm()
    return render_to_response('finances/register.html', {'form': form, 'title': title}, context_instance=RequestContext(request))

class EditItem(UpdateView):
    model = Item
    fields = ['name', 'cost', 'price', 'stock', 'cat']
    template_name = "finances/item_edit.html"
    success_url = reverse_lazy('finances:item_list')

class DeleteItem(DeleteView):
    model = Item
    success_url = reverse_lazy('finances:item_list')

def add_sale(request):
    if request.method == 'POST':
        form = SalesForm(request.POST)
        if form.is_valid():
            sales = form.save()
            return redirect('home')
    else:
        form = SalesForm()
    return render_to_response('finances/sales.html', {'form': form}, context_instance=RequestContext(request))

def add_purchase(request):
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            purchase = form.save()
            return redirect('home')
    else:
        form = PurchaseForm()
    return render_to_response('finances/purchase.html', {'form': form}, context_instance=RequestContext(request))