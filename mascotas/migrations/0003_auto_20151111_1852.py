# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascotas', '0002_auto_20151111_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascotasperdidas',
            name='recompensa',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
    ]
