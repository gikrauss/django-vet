from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',
    url(r'^proveedores/$', ProviderList.as_view(), name='provider_list'),
    url(r'^proveedores/nuevo/', 'finances.views.add_provider', name='register_provider'),
    url(r'^proveedor/editar/(?P<pk>\d+)/$', EditProvider.as_view(), name='edit_provider'),
    url(r'^proveedor/borrar/(?P<pk>\d+)/$', DeleteProvider.as_view(), name='delete_provider'),
    url(r'^proveedor/(?P<pk>\d+)/$', ProviderDetails.as_view(), name='provider_details'),    
    url(r'^items/$', ItemList.as_view(), name='item_list'),
    url(r'^items/nuevo/', 'finances.views.add_item', name='register_item'),
    url(r'^item/editar/(?P<pk>\d+)/$', EditItem.as_view(), name='edit_item'),
    url(r'^item/borrar/(?P<pk>\d+)/$', DeleteItem.as_view(), name='delete_item'),
    url(r'^ventas/$', 'finances.views.add_sale', name='add_sale'),
    url(r'^compras/$', 'finances.views.add_purchase', name='add_purchase'),
)