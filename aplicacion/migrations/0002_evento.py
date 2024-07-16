# Generated by Django 5.0.6 on 2024-07-16 21:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('fecha_inicio', models.DateField()),
                ('fecha_final', models.DateField()),
                ('capacidad', models.IntegerField()),
                ('ingresos', models.FloatField()),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicacion.hotel')),
            ],
        ),
    ]