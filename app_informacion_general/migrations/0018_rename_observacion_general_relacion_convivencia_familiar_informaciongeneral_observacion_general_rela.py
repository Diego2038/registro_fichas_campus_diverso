# Generated by Django 4.2.1 on 2024-05-07 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_informacion_general', '0017_profesionalquebrindoatencion_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='informaciongeneral',
            old_name='observacion_general_relacion_convivencia_familiar',
            new_name='observacion_general_relacion_convivencia_vivienda',
        ),
    ]