from django.db import models
from datetime import date
from smart_selects.db_fields import ChainedForeignKey
from clinic.models import Client
from localflavor.ar import ar_provinces


CAT = (
    ('S', 'Servicio'),
    ('P', 'Producto'),
    ('V', 'Vacuna'),
)

class Item(models.Model):
    name = models.CharField(max_length=200, verbose_name='nombre producto')
    cost = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name='costo')
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name='precio')
    stock = models.IntegerField(verbose_name='stock')
    cat = models.CharField(max_length=1, choices=CAT, verbose_name='categoria')

    def __unicode__(self):
        return '%s' %(self.name)

    class Meta:
        verbose_name = 'producto'

class Provider(models.Model):
    name = models.CharField(max_length=200, verbose_name='proveedor')
    phone = models.CharField(max_length=200, verbose_name='telefono')
    email = models.EmailField(max_length=200, verbose_name='email')
    contact = models.CharField(null=True, blank=True, max_length=200, verbose_name='contacto')

    def __unicode__(self):
        return '%s' %(self.name)

    class Meta:
        verbose_name = 'proveedor'
        verbose_name_plural = 'proveedores'

PAY = (
    ('E', 'Efectivo'),
    ('T', 'Tarjeta'),
    ('Ch', 'Cheque'),
    ('CC', 'Cuenta Corriente'),
)

class Sales(models.Model):
    date = models.DateField(default=date.today, verbose_name='fecha')
    client = models.ForeignKey(Client, related_name='sells')
    item = models.ForeignKey(Item, related_name='item', verbose_name='producto')
    cant = models.IntegerField(verbose_name='cantidad')
    pay_type = models.CharField(null=True, max_length=1, choices=PAY, verbose_name='forma de pago')

    def __unicode__(self):
        return '%s %s %s' %(self.date, self.client, self.item)

    class Meta:
        verbose_name = 'venta'

class Buy(models.Model):
    date = models.DateField(default=date.today, verbose_name='fecha')
    provider = models.ForeignKey(Provider, related_name='purchases')
    item = models.ForeignKey(Item, null=True, related_name='purchase', verbose_name='producto')
    cant = models.IntegerField(verbose_name='cantidad')
    pay_type = models.CharField(null=True, max_length=1, choices=PAY, verbose_name='forma de pago')
#    cost = models.ForeignKey(Item, related_name='cost', verbose_name='precio')

    def __unicode__(self):
        return '%s %s %s' %(self.date, self.provider, self.item)

    class Meta:
        verbose_name = 'compra'
