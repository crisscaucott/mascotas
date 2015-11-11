# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FotosCazaRecompensas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('imagen', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'fotos_cazarecompensa',
            },
        ),
        migrations.CreateModel(
            name='FotosMascota',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('imagen', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'fotos_mascota',
            },
        ),
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('raza', models.CharField(max_length=20)),
                ('color', models.CharField(max_length=20)),
                ('sexo', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'mascota',
            },
        ),
        migrations.CreateModel(
            name='MascotaCazaRecompensa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'db_table': 'mascota_cazarecompensa',
            },
        ),
        migrations.CreateModel(
            name='MascotasPerdidas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_perdido', models.DateTimeField()),
                ('fecha_encontrado', models.DateTimeField(blank=True)),
                ('dir_perdido', models.CharField(max_length=60)),
                ('dir_encontrado', models.CharField(max_length=60, blank=True)),
                ('recompensa', models.CharField(max_length=20)),
                ('info_adicional', models.TextField()),
                ('mascota', models.ForeignKey(to='mascotas.Mascota')),
            ],
            options={
                'db_table': 'mascotas_perdidas',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'usuario',
            },
        ),
        migrations.AddField(
            model_name='mascotacazarecompensa',
            name='mascota_perdida',
            field=models.ForeignKey(to='mascotas.MascotasPerdidas'),
        ),
        migrations.AddField(
            model_name='mascotacazarecompensa',
            name='usuario',
            field=models.ForeignKey(to='mascotas.Usuario'),
        ),
        migrations.AddField(
            model_name='fotosmascota',
            name='mascota',
            field=models.ForeignKey(to='mascotas.Mascota'),
        ),
        migrations.AddField(
            model_name='fotoscazarecompensas',
            name='mascota_caza',
            field=models.ForeignKey(to='mascotas.MascotaCazaRecompensa'),
        ),
    ]
