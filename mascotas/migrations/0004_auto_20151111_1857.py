# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascotas', '0003_auto_20151111_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascotacazarecompensa',
            name='mascota_perdida',
            field=models.ForeignKey(blank=True, to='mascotas.MascotasPerdidas', null=True),
        ),
        migrations.AlterField(
            model_name='mascotasperdidas',
            name='dir_encontrado',
            field=models.CharField(max_length=60, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='mascotasperdidas',
            name='fecha_encontrado',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
