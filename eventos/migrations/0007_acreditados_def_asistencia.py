# Generated by Django 4.1.5 on 2023-07-18 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0006_acreditados_def_acreditado_por'),
    ]

    operations = [
        migrations.AddField(
            model_name='acreditados_def',
            name='asistencia',
            field=models.BooleanField(default=False),
        ),
    ]
