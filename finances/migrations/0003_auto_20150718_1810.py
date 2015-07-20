# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0002_auto_20150718_1753'),
    ]

    operations = [
        migrations.AddField(
            model_name='sales',
            name='cant',
            field=models.IntegerField(default='0', max_length=3, verbose_name=b'cantidad'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sales',
            name='client',
            field=models.ForeignKey(verbose_name=b'cliente', to='clinic.Client'),
        ),
        migrations.AlterField(
            model_name='sales',
            name='item',
            field=models.ForeignKey(verbose_name=b'producto', to='finances.Item'),
        ),
    ]
