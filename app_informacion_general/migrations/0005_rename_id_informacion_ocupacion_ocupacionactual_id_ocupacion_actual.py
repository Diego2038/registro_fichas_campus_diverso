# Generated by Django 4.2.1 on 2023-06-06 05:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_informacion_general', '0004_rename_informacionocupacion_ocupacionactual_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ocupacionactual',
            old_name='id_informacion_ocupacion',
            new_name='id_ocupacion_actual',
        ),
    ]
