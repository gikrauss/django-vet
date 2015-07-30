# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0002_auto_20150729_1735'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicalrecord',
            name='attached',
            field=models.FileField(upload_to=b'attach/', null=True, verbose_name=b'adjunto', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='medicalrecord',
            name='patient',
            field=models.ForeignKey(related_name=b'history', to='clinic.Patient'),
        ),
    ]
