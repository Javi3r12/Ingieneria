# Generated by Django 5.0.6 on 2024-06-24 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_solicitudes_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitudes',
            name='correo',
            field=models.EmailField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
