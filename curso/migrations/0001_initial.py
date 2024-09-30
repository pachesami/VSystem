# Generated by Django 5.1.1 on 2024-09-30 04:36

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
                ('estudiantes', models.ManyToManyField(blank=True, related_name='curso', to='persona.persona')),
            ],
        ),
    ]
