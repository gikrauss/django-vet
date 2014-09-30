from django.db import models


class Client(models.Model):
  firstname = models.CharField(max_length=200)
  lastname = models.CharField(max_length=200, null=True, blank=True)
  email = models.EmailField(max_length=200, null=True, blank=True)

  def __unicode__(self):
    return "%s %s" % [self.firstname, self.lastname]


class Specie(models.Model):
  name = models.CharField(max_length=200)

  def __unicode__(self):
    return self.name


class Breed(models.Model):
  name = models.CharField(max_length=200)
  specie = models.ForeignKey(Specie)

  def __unicode__(self):
    return self.name


class Gender(models.Model):
  name = models.CharField(max_length=200)

  def __unicode__(self):
    return self.name


class Patient(models.Model):
  name = models.CharField(max_length=200)
  owner = models.ForeignKey(Client)
  breed = models.ForeignKey(Breed, null=True)
  gender = models.ForeignKey(Gender, null=True)
  birthday = models.DateField(null=True)

  def __unicode__(self):
    return self.name


