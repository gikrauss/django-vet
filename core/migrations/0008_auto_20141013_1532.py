# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_address_client'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhoneNumber',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.CharField(max_length=200, verbose_name=b'n\xc3\xbamero')),
                ('number_type', models.CharField(max_length=1, verbose_name=b'tipo', choices=[(b'C', b'Celular'), (b'F', b'Fijo'), (b'W', b'Trabajo')])),
                ('client', models.ForeignKey(to='core.Client')),
            ],
            options={
                'verbose_name': 'n\xfamero de tel\xe9fono',
                'verbose_name_plural': 'n\xfameros de tel\xe9fono',
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name': 'direcci\xf3n', 'verbose_name_plural': 'direcciones'},
        ),
    ]
