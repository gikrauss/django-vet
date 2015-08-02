# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0006_auto_20150731_0947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(max_length=6, null=True, verbose_name=b'sexo', choices=[(b'Macho', b'Macho'), (b'Hembra', b'Hembra')]),
        ),
    ]
