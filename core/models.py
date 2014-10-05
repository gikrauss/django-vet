# -*- coding: utf-8 -*-

from django.db import models
from datetime import datetime


class Client(models.Model):
  firstname = models.CharField(max_length=200, verbose_name='nombre')
  lastname = models.CharField(max_length=200, null=True, blank=True, verbose_name='apellido')
  email = models.EmailField(max_length=200, null=True, blank=True, verbose_name='email')

  def __unicode__(self):
    return "%s %s" % (self.firstname, self.lastname)


class Specie(models.Model):
  name = models.CharField(max_length=200, verbose_name='nombre')

  def __unicode__(self):
    return self.name


class Breed(models.Model):
  name = models.CharField(max_length=200, verbose_name='nombre')
  specie = models.ForeignKey(Specie)

  def __unicode__(self):
    return self.name


class Gender(models.Model):
  name = models.CharField(max_length=200, verbose_name='nombre')

  def __unicode__(self):
    return self.name


class Patient(models.Model):
  name = models.CharField(max_length=200, verbose_name='nombre')
  owner = models.ForeignKey(Client, verbose_name='dueño')
  breed = models.ForeignKey(Breed, null=True, verbose_name='raza')
  gender = models.ForeignKey(Gender, null=True, verbose_name='sexo')
  birthday = models.DateField(null=True, verbose_name='fecha de nacimiento')
  identifier = models.CharField(null=True, max_length=200, verbose_name='identificador')
  initial_anamnesis = models.TextField(null=True, verbose_name='anamnesis inicial')

  def __unicode__(self):
    return self.name


class MedicalRecord(models.Model):
  date = models.DateTimeField(default=datetime.now, verbose_name='fecha')
  patient = models.ForeignKey(Patient)
  anamnesis = models.TextField(null=True, verbose_name='anamnesis')
  exam = models.TextField(null=True, verbose_name='examen')
  diagnostic = models.TextField(null=True, verbose_name='diagnóstico')
  ttd = models.TextField(null=True, verbose_name='ttd')
