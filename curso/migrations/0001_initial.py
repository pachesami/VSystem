# Generated by Django 5.1.1 on 2024-10-14 20:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('persona', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('duracion', models.IntegerField()),
                ('capacidadMaxima', models.IntegerField()),
                ('profesor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='persona.persona')),
            ],
        ),
        migrations.CreateModel(
            name='EstudianteYCurso',
            fields=[
                ('dni', models.CharField(default='SIN_DNI', max_length=20, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('fechadeinicio', models.DateField()),
                ('fechefinal', models.DateField()),
                ('estado', models.CharField(max_length=100)),
                ('nota_final', models.FloatField()),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curso.curso')),
            ],
        ),
    ]
