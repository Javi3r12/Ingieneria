# Generated by Django 5.0.6 on 2024-06-24 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_estadosoli_idestado_alter_solicitudes_idestado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estadosoli',
            name='idEstado',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
