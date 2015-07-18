from django.db import models
from datetime import date
from smart_selects.db_fields import ChainedForeignKey


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
        return '%s %s %s %s' %(self.name, self.cost, self.price, self.stock)

    class Meta:
        verbose_name = 'producto'