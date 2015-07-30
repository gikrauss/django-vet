# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='image',
            field=models.ImageField(upload_to=b'patient_photo', null=True, verbose_name=b'im\xc3\xa1gen', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='address',
            name='client',
            field=models.ForeignKey(related_name=b'addresses', to='clinic.Client'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='owner',
            field=models.ForeignKey(related_name=b'pets', verbose_name=b'due\xc3\xb1o', to='clinic.Client'),
        ),
        migrations.AlterField(
            model_name='phonenumber',
            name='client',
            field=models.ForeignKey(related_name=b'phone_numbers', to='clinic.Client'),
        ),
    ]
