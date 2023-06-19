# Generated by Django 4.2.1 on 2023-06-19 01:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_registro', '0006_persona_ciudad_nacimiento_persona_ciudad_residencia_and_more'),
        ('app_informacion_general', '0015_alter_informaciongeneral_observacion_horario_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='informaciongeneral',
            name='id_persona',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='informacion_general', to='app_registro.persona'),
        ),
    ]
