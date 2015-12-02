# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascotas', '0006_auto_20151111_1916'),
    ]

    operations = [
        migrations.AddField(
            model_name='mascota',
            name='animal',
            field=models.CharField(default=None, max_length=30),
            preserve_default=False,
        ),
    ]
