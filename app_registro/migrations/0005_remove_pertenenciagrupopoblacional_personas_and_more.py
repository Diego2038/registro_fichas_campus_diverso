# Generated by Django 4.2.1 on 2023-06-04 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_registro', '0004_remove_persona_pertenencia_grupo_poblacional'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pertenenciagrupopoblacional',
            name='personas',
        ),
        migrations.AddField(
            model_name='persona',
            name='pertenencia_grupo_poblacional',
            field=models.ManyToManyField(max_length=300, related_name='personas', to='app_registro.pertenenciagrupopoblacional'),
        ),
    ]
