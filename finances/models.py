from django.db import models
from datetime import date
from smart_selects.db_fields import ChainedForeignKey
from clinic.models import Client


CAT = (
    ('S', 'Servicio'),
    ('P', 'Producto'),
)

class Item(models.Model):
    name = models.CharField(max_length=200, verbose_name='nombre producto')
    cost = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name='costo')
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name='precio')
    stock = models.IntegerField(max_length=200, verbose_name='stock')
    cat = models.CharField(max_length=1, choices=CAT, verbose_name='categoria')

    def __unicode__(self):
        return '%s' %(self.name)

    class Meta:
        verbose_name = 'producto'

class Sales(models.Model):
    date = models.DateField(default=date.today, verbose_name='fecha')
    client = models.ForeignKey(Client, verbose_name='cliente')
    item = models.ForeignKey(Item, verbose_name='producto')
    cant = models.IntegerField(max_length=3, verbose_name='cantidad')
#    price = Item.price


    def __unicode__(self):
        return '%s %s %s' %(self.date, self.client, self.item)

    class Meta:
        verbose_name = 'venta'