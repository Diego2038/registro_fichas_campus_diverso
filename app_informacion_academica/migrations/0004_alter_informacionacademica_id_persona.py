# Generated by Django 4.2.1 on 2023-07-09 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_registro', '0006_persona_ciudad_nacimiento_persona_ciudad_residencia_and_more'),
        ('app_informacion_academica', '0003_alter_informacionacademica_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='informacionacademica',
            name='id_persona',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='informacion_academica', to='app_registro.persona'),
        ),
    ]
