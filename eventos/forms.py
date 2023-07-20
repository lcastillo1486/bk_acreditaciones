from django.forms import ModelForm
from django.forms import widgets
from django import forms
from django.contrib.auth.models import User
from .models import bkt_eventos

class formEvento(forms.Form):
    nombre_evento = forms.CharField(max_length=100, label='Nombre del Evento:')
    lugar_evento = forms.CharField(max_length=100, label= 'Lugar Evento:')
    fecha_evento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label='Fecha:'    )
