# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascotas', '0008_auto_20151202_2158'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotosmascota',
            name='deleted_at',
            field=models.BooleanField(default=False),
        ),
    ]
