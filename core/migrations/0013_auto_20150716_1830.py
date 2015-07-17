# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_vaccine'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vaccine',
            options={'verbose_name': 'Vacuna'},
        ),
        migrations.AddField(
            model_name='vaccine',
            name='next_vac',
            field=models.CharField(max_length=1, null=True, verbose_name=b'pr\xc3\xb3xima vacuna', choices=[(b'Q', b'Quintuple'), (b'S', b'Sextuple'), (b'R', b'Rabia'), (b'T', b'Tos de las perreras')]),
            preserve_default=True,
        ),
    ]
