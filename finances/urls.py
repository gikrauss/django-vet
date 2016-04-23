from django.conf.urls import patterns, include, url
from .views import ProviderList, EditProvider, DeleteProvider, ItemList, EditItem, DeleteItem

urlpatterns = patterns('',
    url(r'^finanzas/proveedores/$', ProviderList.as_view(), name='provider_list'),
    url(r'^finanzas/proveedores/nuevo/', 'finances.views.add_provider', name='register_provider'),
    url(r'^finanzas/proveedor/editar/(?P<pk>\d+)/$', EditProvider.as_view(), name='edit_provider'),
    url(r'^finanzas/proveedor/borrar/(?P<pk>\d+)/$', DeleteProvider.as_view(), name='delete_provider'),
    url(r'^finanzas/ventas/$', 'finances.views.add_sale', name='add_sale'),
    url(r'^finanzas/items/$', ItemList.as_view(), name='item_list'),
    url(r'^finanzas/items/nuevo/', 'finances.views.add_item', name='register_item'),
    url(r'^finanzas/item/editar/(?P<pk>\d+)/$', EditItem.as_view(), name='edit_item'),
    url(r'^finanzas/item/borrar/(?P<pk>\d+)/$', DeleteItem.as_view(), name='delete_item'),
)