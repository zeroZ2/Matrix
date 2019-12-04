from django import forms
from .models import *

class ClientesForm(forms.Form):
    correo = forms.CharField(label = 'Correo',max_length=100)
    contrasenha = forms.CharField(label = 'Contraseña', max_length=10)
    nombre = forms.CharField(label = 'Nombres',max_length=100)
    apellido = forms.CharField(label = 'Apellidos',max_length=100)
    direccion = forms.CharField(label = 'Direccion',max_length=100)
    telefono = forms.IntegerField(label = 'Telefono')
	
class ProductosForm(forms.Form):
	nombre_prod = forms.CharField(label='Nombre Producto', max_length=100)
	precio_unitario = forms.FloatField(label='Precio')
	descripcion = forms.CharField(label='Descripcion', max_length=500)
	tipo = forms.CharField(label='Tipo', max_length=100)
	image_url = forms.CharField(label='Direccion', max_length=100)
		
