# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0012_patient_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='deworming',
            name='dose',
            field=models.CharField(max_length=200, null=True, verbose_name=b'dosis', blank=True),
            preserve_default=True,
        ),
    ]
