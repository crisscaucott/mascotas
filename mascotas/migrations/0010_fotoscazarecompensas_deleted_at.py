# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascotas', '0009_fotosmascota_deleted_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotoscazarecompensas',
            name='deleted_at',
            field=models.BooleanField(default=False),
        ),
    ]
