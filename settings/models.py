from __future__ import unicode_literals
from django.db import models
from smart_selects.db_fields import ChainedForeignKey

class Specie(models.Model):
  name = models.CharField(max_length=200, verbose_name='nombre')

  def __unicode__(self):
    return self.name

  class Meta:
    verbose_name = 'especie'
    ordering = ['name']

class Breed(models.Model):
  name = models.CharField(max_length=200, verbose_name='nombre')
  specie = models.ForeignKey(Specie)

  def __unicode__(self):
    return self.name

  class Meta:
    verbose_name = 'raza'
    ordering = ['name']

class Vac_Type(models.Model):
  name = models.CharField(max_length=200, verbose_name='tipo de vacuna')
  description = models.CharField(max_length=200, null=True, blank=True, verbose_name='descripcion')

  def __unicode__(self):
    return self.name

  class Meta:
    verbose_name = 'tipo de vacuna'
    verbose_name_plural = 'tipos de vacunas'
    ordering = ['name']
