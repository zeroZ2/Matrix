from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

from .models import *
from .forms import *

from django.views.decorators.csrf import csrf_exempt

def  base(request):
	return render(request,'base.html')

def  inicio(request):
	return render(request,'index.html')


def productosListC(request,id_clien):
	todosProductos=Productos.objects.all()
	return render(request,'productosListC.html',{'productos':todosProductos})
def  loginC(request):
	if request.method == 'POST':
		acces="no"
		username = request.POST["email"]
		password = request.POST["password"]
		todosId = Clientes.objects.values_list('id_cliente',flat=True)
		todosCorreo = Clientes.objects.values_list('correo', flat=True)
		todosPass = Clientes.objects.values_list('contrasenha', flat=True)
		mxx=len(todosCorreo)
		for x in range(0,mxx):
			if (todosCorreo[x] == username and todosPass[x] == password):
				id_clien=todosId[x]
				acces="yes"
				todosCorreo=[]
				todosPass=[]
				
				break

		if acces=="yes":
			return redirect('productosListC',{'id_clien':id_clien})
		else:
			return render(request,'loginC.html')
	else:
		return render(request,'loginC.html')

def  loginE(request):
	if request.method == 'POST':
		acces1="no"
		username1 = request.POST["emails"]
		password1 = request.POST["passwords"]
		todosId1= Empleados.objects.values_list('id_empleado',flat=True)
		todosCorreo1 = Empleados.objects.values_list('correo', flat=True)
		todosPass1 = Empleados.objects.values_list('contrasenha', flat=True)
		mxx1=len(todosCorreo1)
		for x in range(0,mxx1):
			if (todosCorreo1[x] == username1 and todosPass1[x] == password1):
				acces1="yes"
				id_em=todosId1[x]
				todosCorreo1=[]
				todosPass1=[]
				
				break

		if acces1=="yes":
			return redirect('inicioE',{'id_em':id_em})
		else:
			return render(request,'loginE.html')
	else:
		return render(request,'loginE.html')
def inicioE(request,id_em):
	return render(request,'inicioE.html')
def registrarCliente(request):
	if request.method == 'POST':
		form = ClientesForm(request.POST)
		if form.is_valid():
			cliente = Clientes()
			cliente.correo = form.cleaned_data['correo']
			cliente.contrasenha = form.cleaned_data['contrasenha']
			cliente.nombre = form.cleaned_data['nombre']
			cliente.apellido = form.cleaned_data['apellido']
			cliente.direccion = form.cleaned_data['direccion']
			cliente.telefono = form.cleaned_data['telefono']
			cliente.save()
			return render(request,'loginC.html')
	else:
		form = ClientesForm
		todosCorreo = Clientes.objects.values_list('correo', flat=True)
		todosClientes = Clientes.objects.all()
		return render(request, 'registrarC.html', {'clientes':todosClientes,'correos':todosCorreo, 'form':form})