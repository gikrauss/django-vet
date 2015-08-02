# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0005_auto_20150730_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(max_length=1, null=True, verbose_name=b'sexo', choices=[(b'Macho', b'Macho'), (b'Hembra', b'Hembra')]),
        ),
        migrations.DeleteModel(
            name='Gender',
        ),
    ]
