# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascotas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascotacazarecompensa',
            name='mascota_perdida',
            field=models.ForeignKey(to='mascotas.MascotasPerdidas', blank=True),
        ),
        migrations.AlterField(
            model_name='mascotasperdidas',
            name='recompensa',
            field=models.CharField(max_length=20, blank=True),
        ),
    ]
