
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django import forms
from django.db import models
from io import BytesIO
import datetime

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, legal, portrait
from reportlab.lib.units import cm

# Create your views here.
def tecladopersonal(request):
    return render(request,'acredpersonal.html')