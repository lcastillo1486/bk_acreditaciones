
from django.db import models

# Create your models here.
class bkt_eventos(models.Model):
    nombre_evento = models.CharField(max_length=200, blank=False, null=False)
    lugar_evento = models.CharField(max_length=200, blank=False, null=False)
    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_evento = models.DateField()
    evento_activo = models.BooleanField(default=True)
    num_cargas = models.IntegerField(default=0)
    cargas_max = models.IntegerField(default=3)
    acreditacion_activa = models.BooleanField(default=False) 

class acreditados_tmp(models.Model):
    id_evento_id = models.CharField(max_length=50, blank=True, null=True)
    nombre_persona = models.CharField(max_length=200, blank=False, null=False)
    apellido_persona = models.CharField(max_length=200, blank=False, null=False)
    tipo_doc = models.CharField(max_length=5, blank=False, null=False)
    numero_doc = models.CharField(max_length=10, blank=False, null=False)
    empresa = models.CharField(max_length=200, blank=True, null=True)
    cargo = models.CharField(max_length=50, blank=True, null=True)
    zona_acceso = models.CharField(max_length=50, blank=False, null=False)
    color_zona = models.CharField(max_length=50, blank=True, null=True)

class acreditados_def(models.Model):
    id_evento = models.ForeignKey(bkt_eventos, on_delete = models.DO_NOTHING)
    nombre_persona = models.CharField(max_length=200, blank=False, null=False)
    apellido_persona = models.CharField(max_length=200, blank=False, null=False)
    tipo_doc = models.CharField(max_length=5, blank=False, null=False)
    numero_doc = models.CharField(max_length=10, blank=False, null=False)
    empresa = models.CharField(max_length=200, blank=True, null=True)
    cargo = models.CharField(max_length=50, blank=True, null=True)
    zona_acceso = models.CharField(max_length=50, blank=False, null=False)
    color_zona = models.CharField(max_length=50, blank=True, null=True)
    acreditado = models.BooleanField(default=False, blank=False, null=False)
    acreditado_por = models.CharField(max_length=50, blank=True, null=True)
    asistencia = models.BooleanField(default=False)
    evento_cerrado = models.BooleanField(default=False)
    hora = models.CharField(max_length=6, blank=True, null=True)

class acreditadorEvento(models.Model):
    usuario = models.CharField(max_length=50, blank=True, null=True)
    evento = models.CharField(max_length=50, blank=True, null=True)
    cerrado = models.BooleanField(default=False)

class inventarioBrazalete(models.Model):
    id_evento = models.IntegerField()
    nombre_brazalete = models.CharField(max_length=50)
    cantidad_brazalete = models.IntegerField()
    cantidad_entregada = models.IntegerField(default=0)
    cantidad_resta = models.IntegerField(default=0)
    evento_cerrado = models.BooleanField(default=False)

class inventarioBrazaleteAcreditardor(models.Model):
    id_evento = models.IntegerField()
    nombre_acreditador = models.CharField(max_length=50)
    nombre_brazalete = models.CharField(max_length=50)
    cantidad_brazalete = models.IntegerField(default=0)
    cantidad_entregada = models.IntegerField(default=0)
    cantidad_resta = models.IntegerField(default=0)
    evento_cerrado = models.BooleanField(default=False)