from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',
	url(r'^raza/$', BreedList.as_view(), name='breed_conf'),
    url(r'^raza/nuevo/', 'settings.views.add_breed', name='breed_conf_add'),
    url(r'^raza/editar/(?P<pk>\d+)/$', EditBreed.as_view(), name='edit_breed'),
    url(r'^raza/borrar/(?P<pk>\d+)/$', DeleteBreed.as_view(), name='delete_breed'),
    url(r'^especie/$', SpecieList.as_view(), name='specie_conf'),
    url(r'^especie/nuevo/', 'settings.views.add_specie', name='specie_conf_add'),
    url(r'^especie/editar/(?P<pk>\d+)/$', EditSpecie.as_view(), name='edit_specie'),
    url(r'^especie/borrar/(?P<pk>\d+)/$', DeleteSpecie.as_view(), name='delete_specie'),
    url(r'^tipo_vac/$', Vac_TypeList.as_view(), name='vac_conf'),
    url(r'^tipo_vac/nuevo/', 'settings.views.add_vac_type', name='vac_conf_add'),
    url(r'^tipo_vac/editar/(?P<pk>\d+)/$', EditVac_Type.as_view(), name='edit_vac_type'),
    url(r'^tipo_vac/borrar/(?P<pk>\d+)/$', DeleteVac_Type.as_view(), name='delete_vac_type'),
)