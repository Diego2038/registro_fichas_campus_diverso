# Generated by Django 4.2.1 on 2024-06-21 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_profesional', '0009_profesional_first_name_profesional_is_active_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profesional',
        ),
    ]