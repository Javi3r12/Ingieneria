# Generated by Django 5.0.6 on 2024-06-23 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='estadoSoli',
            fields=[
                ('id_estado', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_estado', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='estadoSolicitud',
        ),
    ]