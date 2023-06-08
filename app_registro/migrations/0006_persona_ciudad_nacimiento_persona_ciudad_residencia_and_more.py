# Generated by Django 4.2.1 on 2023-06-08 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_registro', '0005_remove_pertenenciagrupopoblacional_personas_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='ciudad_nacimiento',
            field=models.CharField(default='Ciudad no especificada', max_length=100),
        ),
        migrations.AddField(
            model_name='persona',
            name='ciudad_residencia',
            field=models.CharField(default='Ciudad no especificada', max_length=100),
        ),
        migrations.AddField(
            model_name='persona',
            name='corregimiento_nacimiento',
            field=models.CharField(default='Corregimiento no especificado', max_length=100),
        ),
        migrations.AddField(
            model_name='persona',
            name='corregimiento_residencia',
            field=models.CharField(default='Corregimiento no especificado', max_length=100),
        ),
        migrations.AddField(
            model_name='persona',
            name='nombre_persona_de_confianza',
            field=models.TextField(default='Pepito Perez'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='persona',
            name='relacion_persona_de_confianza',
            field=models.TextField(default='Amig@'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='persona',
            name='telefono_persona_de_confianza',
            field=models.TextField(default='3167890987'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='persona',
            name='departamento_nacimiento',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='persona',
            name='municipio_nacimiento',
            field=models.CharField(default='Municipio no especificado', max_length=100),
        ),
        migrations.AlterField(
            model_name='persona',
            name='municipio_residencia',
            field=models.CharField(default='Municipio no especificado', max_length=100),
        ),
        migrations.AlterField(
            model_name='persona',
            name='pais_nacimiento',
            field=models.CharField(max_length=100),
        ),
    ]