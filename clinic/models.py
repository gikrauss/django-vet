# -*- coding: utf-8 -*-

from django.db import models
from datetime import date
from smart_selects.db_fields import ChainedForeignKey
from localflavor.ar import ar_provinces


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
    return "%s %s" % (self.firstname, self.lastname)

  class Meta:
    verbose_name = 'cliente'


class Address(models.Model):
  address = models.CharField(max_length=200, verbose_name='calle y número')
  city = models.CharField(max_length=200, verbose_name='ciudad')
  state = models.CharField(max_length=1, choices=ar_provinces.PROVINCE_CHOICES, verbose_name='provincia')
  postal = models.CharField(max_length=6, null=True, verbose_name='código postal')
  client = models.ForeignKey(Client)

  def __unicode__(self):
    return "%s, %s, %s, %s" % (self.address, self.city, self.state, self.postal)

  class Meta:
    verbose_name = 'dirección'
    verbose_name_plural = 'direcciones'


class PhoneNumber(models.Model):
  number = models.CharField(max_length=200, verbose_name='número')
  number_type = models.CharField(max_length=1, choices=PHONE_TYPE, verbose_name='tipo')
  client = models.ForeignKey(Client)

  class Meta:
    verbose_name = 'número de teléfono'
    verbose_name_plural = 'números de teléfono'


class Specie(models.Model):
  name = models.CharField(max_length=200, verbose_name='nombre')

  def __unicode__(self):
    return self.name

  class Meta:
    verbose_name = 'especie'


class Breed(models.Model):
  name = models.CharField(max_length=200, verbose_name='nombre')
  specie = models.ForeignKey(Specie)

  def __unicode__(self):
    return self.name

  class Meta:
    verbose_name = 'raza'


class Gender(models.Model):
  name = models.CharField(max_length=200, verbose_name='nombre')

  def __unicode__(self):
    return self.name

  class Meta:
    verbose_name = 'sexo'


class Patient(models.Model):
  name = models.CharField(max_length=200, verbose_name='nombre')
  owner = models.ForeignKey(Client, verbose_name='dueño')
  specie = models.ForeignKey(Specie, null=True, verbose_name='especie')
  breed = ChainedForeignKey(Breed, null=True, chained_field="specie", chained_model_field="specie", 
        show_all=False, auto_choose=True, verbose_name='raza')
  gender = models.ForeignKey(Gender, null=True, verbose_name='sexo')
  neutered = models.BooleanField(default=False, verbose_name='castrado')
  birthday = models.DateField(null=True, verbose_name='fecha de nacimiento')
  weight = models.CharField(null=True, blank=True, max_length=10, verbose_name='peso')
  identifier = models.CharField(null=True, blank=True, max_length=200, verbose_name='identificador')
#  image = models.ImageField(null=True, blank=True, upload_to='patient_photo', verbose_name='imágen')
  initial_anamnesis = models.TextField(null=True, blank=True, verbose_name='anamnesis inicial')

  def age(slef):
    today = date.today()
    return today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month, born.day))

  def __unicode__(self):
    return self.name

  class Meta:
    verbose_name = 'paciente'


class MedicalRecord(models.Model):
  date = models.DateField(default=date.today, verbose_name='fecha')
  patient = models.ForeignKey(Patient)
  temp = models.CharField(max_length=5, null=True, blank=True, verbose_name='temp')
  anamnesis = models.TextField(null=True, blank=True, verbose_name='anamnesis')
  exam = models.TextField(null=True, blank=True, verbose_name='examen')
  diagnostic = models.TextField(null=True, blank=True, verbose_name='diagnóstico')
  tto = models.TextField(null=True, blank=True, verbose_name='indicaciones')
#  attached = models.FileField(null=True, blank=True, upload_to='attach/', verbose_name='adjunto')

  class Meta:
    verbose_name = 'historia clínica'


VAC_TYPE = (
  ('Q', 'Quintuple'),
  ('S', 'Sextuple'),
  ('R', 'Rabia'),
  ('T', 'Tos de las perreras'),
  )

class Vaccine(models.Model):
  vac_type = models.CharField(max_length=1, choices=VAC_TYPE, verbose_name='tipo')
  patient = models.ForeignKey(Patient)
  marca = models.CharField(max_length=10, verbose_name='marca')
  date = models.DateField(default=date.today, verbose_name='fecha de vacunación')
  expire_date = models.DateField(verbose_name='fecha de vencimiento')
  next_vac = models.CharField(null=True, max_length=1, choices=VAC_TYPE, verbose_name='próxima vacuna')

  class Meta:
    verbose_name='Vacuna'