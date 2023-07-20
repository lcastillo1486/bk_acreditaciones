# Generated by Django 4.1.5 on 2023-07-14 00:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bk_eventos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_evento', models.CharField(max_length=200)),
                ('lugar_evento', models.CharField(max_length=200)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('fecha_evento', models.DateField()),
                ('evento_activo', models.BooleanField(default=True)),
                ('num_cargas', models.IntegerField(default=0)),
                ('cargas_max', models.IntegerField(default=3)),
                ('acreditacion_activa', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='acreditados_tmp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_persona', models.CharField(max_length=200)),
                ('apellido_persona', models.CharField(max_length=200)),
                ('tipo_doc', models.CharField(max_length=5)),
                ('numero_doc', models.IntegerField(max_length=10)),
                ('cargo', models.CharField(blank=True, max_length=50, null=True)),
                ('zona_acceso', models.CharField(max_length=50)),
                ('id_evento', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='eventos.bk_eventos')),
            ],
        ),
        migrations.CreateModel(
            name='acreditados_def',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_persona', models.CharField(max_length=200)),
                ('apellido_persona', models.CharField(max_length=200)),
                ('tipo_doc', models.CharField(max_length=5)),
                ('numero_doc', models.IntegerField(max_length=10)),
                ('cargo', models.CharField(blank=True, max_length=50, null=True)),
                ('zona_acceso', models.CharField(max_length=50)),
                ('acreditado', models.BooleanField(default=False)),
                ('id_evento', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='eventos.bk_eventos')),
            ],
        ),
    ]
