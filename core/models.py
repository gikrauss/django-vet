from django.db import models


class Client(models.Model):
  name = models.CharField(max_length=200)

  def __unicode__(self):
    return self.name


class Patient(models.Model):
  name = models.CharField(max_length=200)
  owner = models.ForeignKey(Client)

  def __unicode__(self):
    return self.name

