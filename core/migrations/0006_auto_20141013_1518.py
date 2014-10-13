# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20141005_0213'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.CharField(max_length=200, verbose_name=b'calle y n\xc3\xbamero')),
                ('city', models.CharField(max_length=200, verbose_name=b'ciudad')),
                ('state', models.CharField(max_length=1, verbose_name=b'provincia', choices=[('B', 'Buenos Aires'), ('K', 'Catamarca'), ('H', 'Chaco'), ('U', 'Chubut'), ('C', 'Ciudad Aut\xf3noma de Buenos Aires'), ('X', 'C\xf3rdoba'), ('W', 'Corrientes'), ('E', 'Entre R\xedos'), ('P', 'Formosa'), ('Y', 'Jujuy'), ('L', 'La Pampa'), ('F', 'La Rioja'), ('M', 'Mendoza'), ('N', 'Misiones'), ('Q', 'Neuqu\xe9n'), ('R', 'R\xedo Negro'), ('A', 'Salta'), ('J', 'San Juan'), ('D', 'San Luis'), ('Z', 'Santa Cruz'), ('S', 'Santa Fe'), ('G', 'Santiago del Estero'), ('V', 'Tierra del Fuego, Ant\xe1rtida e Islas del Atl\xe1ntico Sur'), ('T', 'Tucum\xe1n')])),
            ],
            options={
                'verbose_name': 'direcci\xf3n',
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='patient',
            name='breed',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'specie', chained_field=b'specie', verbose_name=b'raza', auto_choose=True, to='core.Breed', null=True),
        ),
    ]
