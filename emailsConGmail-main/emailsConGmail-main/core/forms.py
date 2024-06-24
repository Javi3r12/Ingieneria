# forms.py

from django import forms
from .models import estadoSoli

class ContactForm(forms.Form):
    name = forms.CharField(label='Nombre y Apellido', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre y Apellido', 'required': True}))
    destinatarios = forms.EmailField(label='Correo Electrónico', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo Electrónico', 'required': True}))
    subject = forms.CharField(label='Asunto', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Asunto', 'required': True}))
    opcion_estado = forms.ModelChoiceField(label='Estado de la Reparacion   ', queryset=estadoSoli.objects.all(), empty_label='Seleccione un estado', widget=forms.Select(attrs={'class': 'form-control', 'required': True}))
    razon = forms.CharField(label='razon', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Razon de la decicion', 'required': True}))

class EstadoSolicitud(forms.Form):
    name = forms.CharField(label='Nombre', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre y Apellido', 'required': True}))
    destinatarios = forms.EmailField(label='Correo Electrónico', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo Electrónico', 'required': True}))
    detalle = forms.CharField(label='razon', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Razon de la decicion', 'required': True}))
    opcion_estado = forms.ModelChoiceField(label='Estado de la Solicitud', queryset=estadoSoli.objects.all(), empty_label='Seleccione un estado', widget=forms.Select(attrs={'class': 'form-control', 'required': True}))
