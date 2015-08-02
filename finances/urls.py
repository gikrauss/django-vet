from django.conf.urls import patterns, include, url
from .views import ProviderList, EditProvider, DeleteProvider

urlpatterns = patterns('',
    url(r'^finanzas/proveedores/$', ProviderList.as_view(), name='provider_list'),
    url(r'^finanzas/proveedor/editar/(?P<pk>\d+)/$', EditProvider.as_view(), name='edit_provider'),
    url(r'^finanzas/proveedor/borrar/(?P<pk>\d+)/$', DeleteProvider.as_view(), name='delete_provider'),
)