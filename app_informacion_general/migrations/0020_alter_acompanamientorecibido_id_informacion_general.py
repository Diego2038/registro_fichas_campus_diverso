# Generated by Django 4.2.1 on 2024-06-21 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_informacion_general', '0019_alter_informaciongeneral_tiene_eps'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acompanamientorecibido',
            name='id_informacion_general',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='acompanamientos_recibido', to='app_informacion_general.informaciongeneral'),
        ),
    ]
