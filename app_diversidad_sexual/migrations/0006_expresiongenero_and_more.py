# Generated by Django 4.2.1 on 2023-06-05 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_diversidad_sexual', '0005_identidadgenero_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExpresionGenero',
            fields=[
                ('id_expresion_genero', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_expresion_genero', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='diversidadsexual',
            name='expresiones_de_genero',
            field=models.ManyToManyField(max_length=200, to='app_diversidad_sexual.expresiongenero'),
        ),
    ]
