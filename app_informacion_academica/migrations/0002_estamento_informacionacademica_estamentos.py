# Generated by Django 4.2.1 on 2023-06-06 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_informacion_academica', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estamento',
            fields=[
                ('id_estamento', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_estamento', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='informacionacademica',
            name='estamentos',
            field=models.ManyToManyField(max_length=100, to='app_informacion_academica.estamento'),
        ),
    ]
