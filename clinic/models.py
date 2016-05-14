# -*- coding: utf-8 -*-

from django.db import models
from datetime import date
from smart_selects.db_fields import ChainedForeignKey
from localflavor.ar import ar_provinces
from settings.models import Specie, Breed, Vac_Type


PHONE_TYPE = (
  ('C', 'Celular'),
  ('F', 'Fijo'),
  ('W', 'Trabajo'),
  )


class Client(models.Model):
  firstname = models.CharField(max_length=200, verbose_name='nombre')
  lastname = models.CharField(max_length=200, null=True, blank=True, verbose_name='apellido')
  email = models.EmailField(max_length=200, null=True, blank=True, verbose_name='email')

  def __unicode__(self):
    return "%s %s" % (self.lastname, self.firstname)

  class Meta:
    verbose_name = 'cliente'
    ordering = ['lastname']


class Address(models.Model):
  address = models.CharField(max_length=200, verbose_name='calle y número')
  city = models.CharField(max_length=200, verbose_name='ciudad')
  state = models.CharField(max_length=1, choices=ar_provinces.PROVINCE_CHOICES, verbose_name='provincia')
  postal = models.CharField(max_length=6, null=True, verbose_name='código postal')
  client = models.ForeignKey(Client, related_name='addresses')

  def __unicode__(self):
    return "%s, %s, %s, %s" % (self.address, self.city, self.state, self.postal)

  class Meta:
    verbose_name = 'dirección'
    verbose_name_plural = 'direcciones'


class PhoneNumber(models.Model):
  number = models.CharField(max_length=200, verbose_name='número')
  number_type = models.CharField(max_length=1, choices=PHONE_TYPE, verbose_name='tipo')
  client = models.ForeignKey(Client, related_name='phone_numbers')

  class Meta:
    verbose_name = 'número de teléfono'
    verbose_name_plural = 'números de teléfono'

GENDER_TYPE= (
  ('Macho', 'Macho'),
  ('Hembra', 'Hembra')
  )


class Patient(models.Model):
  name = models.CharField(max_length=200, verbose_name='nombre')
  owner = models.ForeignKey(Client, verbose_name='dueño', related_name='pets')
  specie = models.ForeignKey(Specie, null=True, verbose_name='especie')
  breed = ChainedForeignKey(Breed, null=True, chained_field="specie", chained_model_field="specie",
        show_all=False, auto_choose=True, verbose_name='raza')
  gender = models.CharField(max_length=6, choices=GENDER_TYPE, null=True, verbose_name='sexo')
  neutered = models.BooleanField(default=False, verbose_name='castrado')
  birthday = models.DateField(null=True, verbose_name='fecha de nacimiento')
  weight = models.CharField(null=True, blank=True, max_length=10, verbose_name='peso')
  color = models.CharField(null=True, blank=True, max_length=200, verbose_name='pelaje')
  identifier = models.CharField(null=True, blank=True, max_length=200, verbose_name='identificador')
  image = models.ImageField(null=True, blank=True, upload_to='patient_photo', verbose_name='imágen')
  initial_anamnesis = models.TextField(null=True, blank=True, verbose_name='anamnesis inicial')

  def age(self):
    today = date.today()
    return today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month, self.birthday.day))

  def __unicode__(self):
    return self.name

  class Meta:
    verbose_name = 'paciente'
    ordering = ['name']


class MedicalRecord(models.Model):
  patient = models.ForeignKey(Patient, related_name='history')
  date = models.DateField(default=date.today, verbose_name='fecha')
  motive = models.TextField(null=True, blank=True, verbose_name='motivo de consulta')
  temp = models.CharField(max_length=6, null=True, blank=True, verbose_name='temp')
  fc = models.CharField(max_length=6, null=True, blank=True, verbose_name='fc')
  fr = models.CharField(max_length=6, null=True, blank=True, verbose_name='fr')
  tllc = models.CharField(max_length=6, null=True, blank=True, verbose_name='tllc')
  anamnesis = models.TextField(null=True, blank=True, verbose_name='anamnesis')
  exam = models.TextField(null=True, blank=True, verbose_name='examen')
  diagnostic = models.TextField(null=True, blank=True, verbose_name='diagnóstico')
  tto = models.TextField(null=True, blank=True, verbose_name='indicaciones')
  attached = models.FileField(null=True, blank=True, upload_to='attach/', verbose_name='adjunto')

  class Meta:
    verbose_name = 'historia clínica'

class Vaccine(models.Model):
  patient = models.ForeignKey(Patient, related_name='vaccine')
  vac_type = models.ForeignKey(Vac_Type, related_name='vac_type', verbose_name='tipo de vacuna')
  date = models.DateField(default=date.today, verbose_name='fecha de vacunación')
  marca = models.CharField(max_length=20, verbose_name='marca')
  expire_date = models.DateField(verbose_name='fecha de vencimiento')
  next_vac = models.ForeignKey(Vac_Type, verbose_name='próxima vacuna')

  def __unicode__(self):
    return self.marca

  class Meta:
    verbose_name='Vacuna'

class Deworming(models.Model):
  patient = models.ForeignKey(Patient, related_name='deworming')
  date = models.DateField(default=date.today, verbose_name='fecha de desparasitación')
  name = models.CharField(max_length=200, verbose_name='antiparasitario')
  dose = models.CharField(null=True, blank=True, max_length=200, verbose_name='posología')

  def __unicode__(self):
    return self.name

  class Meta:
    verbose_name='Antiparasitario'

class Complementary(models.Model):
  patient = models.ForeignKey(Patient, related_name='complementary')
  name = models.CharField(max_length=200, verbose_name='complementario')
  date = models.DateField(default=date.today, verbose_name='fecha')
  description = models.TextField(null=True, blank=True, verbose_name='descripción')
  attached = models.FileField(null=True, blank=True, upload_to='attach/complementary', verbose_name='adjunto')

  def __unicode__(self):
    return self.name

  class Meta:
    verbose_name='Metodo Complementario'
    verbose_name_plural='Metodos Complementarios'

class Analysis(models.Model):
  patient = models.ForeignKey(Patient, related_name='analysis')
  name = models.CharField(max_length=200, verbose_name='Análisis Sanguineo')
  date = models.DateField(default=date.today, verbose_name='fecha')
  description = models.TextField(null=True, blank=True, verbose_name='descripción')
  attached = models.FileField(null=True, blank=True, upload_to='attach/complementary', verbose_name='adjunto')

  def __unicode__(self):
    return self.name

  class Meta:
    verbose_name='Análisis Sanguineo'
    verbose_name_plural='Análisis Sanguineos'
