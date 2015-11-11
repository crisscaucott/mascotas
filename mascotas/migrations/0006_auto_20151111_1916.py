# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascotas', '0005_mascota_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='usuario',
            field=models.ForeignKey(blank=True, to='mascotas.Usuario', null=True),
        ),
    ]
