# Generated by Django 4.2.1 on 2023-06-20 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_informacion_general', '0016_alter_informaciongeneral_id_persona'),
    ]

    operations = [
        migrations.AlterField(
            model_name='informaciongeneral',
            name='encuentro_inicial',
            field=models.CharField(max_length=100),
        ),
    ]
