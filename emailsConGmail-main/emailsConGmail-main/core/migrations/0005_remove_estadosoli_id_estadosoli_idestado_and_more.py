# Generated by Django 5.0.6 on 2024-06-24 03:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_solicitudes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estadosoli',
            name='id',  # Si idEstado es la nueva clave primaria, probablemente deberías eliminar este campo
        ),
        migrations.AddField(
            model_name='estadosoli',
            name='idEstado',
            field=models.AutoField(db_column='idEstado', primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='solicitudes',
            name='idEstado',
            field=models.ForeignKey(db_column='idEstado', on_delete=django.db.models.deletion.CASCADE, to='core.estadosoli'),
        ),
    ]
