# Generated by Django 4.1.5 on 2023-07-17 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0005_alter_acreditados_def_numero_doc_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='acreditados_def',
            name='acreditado_por',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
