# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascotas', '0007_mascota_animal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mascotacazarecompensa',
            name='mascota_perdida',
        ),
        migrations.AddField(
            model_name='mascotasperdidas',
            name='caza_recompensa',
            field=models.ForeignKey(to='mascotas.MascotaCazaRecompensa', null=True),
        ),
    ]
