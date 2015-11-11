# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascotas', '0004_auto_20151111_1857'),
    ]

    operations = [
        migrations.AddField(
            model_name='mascota',
            name='usuario',
            field=models.ForeignKey(default=None, to='mascotas.Usuario'),
            preserve_default=False,
        ),
    ]
