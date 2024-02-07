# Generated by Django 4.1.5 on 2023-08-19 22:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='acreditadorEvento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(blank=True, max_length=50, null=True)),
                ('evento', models.CharField(blank=True, max_length=50, null=True)),
                ('cerrado', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='acreditados_tmp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_evento_id', models.CharField(blank=True, max_length=50, null=True)),
                ('nombre_persona', models.CharField(max_length=200)),
                ('apellido_persona', models.CharField(max_length=200)),
                ('tipo_doc', models.CharField(max_length=5)),
                ('numero_doc', models.CharField(max_length=10)),
                ('empresa', models.CharField(blank=True, max_length=200, null=True)),
                ('cargo', models.CharField(blank=True, max_length=50, null=True)),
                ('zona_acceso', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='bkt_eventos',
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
            name='inventarioBrazalete',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_evento', models.IntegerField()),
                ('nombre_brazalete', models.CharField(max_length=50)),
                ('cantidad_brazalete', models.IntegerField()),
                ('cantidad_entregada', models.IntegerField(default=0)),
                ('cantidad_resta', models.IntegerField(default=0)),
                ('evento_cerrado', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='inventarioBrazaleteAcreditardor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_evento', models.IntegerField()),
                ('nombre_acreditador', models.CharField(max_length=50)),
                ('nombre_brazalete', models.CharField(max_length=50)),
                ('cantidad_brazalete', models.IntegerField(default=0)),
                ('cantidad_entregada', models.IntegerField(default=0)),
                ('cantidad_resta', models.IntegerField(default=0)),
                ('evento_cerrado', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='acreditados_def',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_persona', models.CharField(max_length=200)),
                ('apellido_persona', models.CharField(max_length=200)),
                ('tipo_doc', models.CharField(max_length=5)),
                ('numero_doc', models.CharField(max_length=10)),
                ('empresa', models.CharField(blank=True, max_length=200, null=True)),
                ('cargo', models.CharField(blank=True, max_length=50, null=True)),
                ('zona_acceso', models.CharField(max_length=50)),
                ('acreditado', models.BooleanField(default=False)),
                ('acreditado_por', models.CharField(blank=True, max_length=50, null=True)),
                ('asistencia', models.BooleanField(default=False)),
                ('evento_cerrado', models.BooleanField(default=False)),
                ('hora', models.CharField(blank=True, max_length=6, null=True)),
                ('id_evento', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='eventos.bkt_eventos')),
            ],
        ),
    ]
