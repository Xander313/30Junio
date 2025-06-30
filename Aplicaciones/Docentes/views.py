from django.shortcuts import render, redirect, get_object_or_404
from .models import Cargo

from django.contrib import messages

# Create your views here.

#05 05 2025 pasos del modelo


#esat duncoion realiza (renderizando el te mpalte) el renderizado de le listado de cargos
def inicio(request):
    lCargos = Cargo.objects.all()
    return render(request, "inicio.html", {'cargos':lCargos})


def nuevoCargo (request):
    return render(request, 'nuevoCargo.html')

def guardarCargo(request):
    nombre = request.POST["nombre"]
    funciones = request.POST["funciones"]
    horario = request.POST["horario"]
    requisitos = request.POST["requisitos"]
    sueldo = request.POST["sueldo"].replace(",",".")
    #Esata es la manera en la que se debe capturar los archivos
    logo = request.FILES.get("logo")

    nuevoCargo = Cargo.objects.create(
        nombre=nombre, 
        funciones=funciones,
        horario=horario, 
        requisitos=requisitos, 
        sueldo=sueldo, 
        logo=logo
        )
    
    messages.success(request, "Hemos guardado el cargo exitosamente")
    return redirect('/')





def eliminarDatosPorId(request, id):
    cEliminar = Cargo.objects.get(id=id)
    cEliminar.delete()
    messages.success(request, "Hemos eliminado el cargo exitosamente")
    return redirect('/')

def editarCargo(request,id):
    cargoEditar = Cargo.objects.get(id=id)
    return render(request, 'editarCargo.html', {'cargoEditar':cargoEditar})



def editarCargoEjecucion(request, id):

    #aqui etamos buscando el cargo a traves de su id que viene como param
    cargoEditar = get_object_or_404(Cargo, id=id)

    #capturamos los valores del formulario de edicion
    nombre = request.POST.get('nombre')
    funciones = request.POST.get('funciones')
    horario = request.POST.get('horario')
    requisitos = request.POST.get('requisitos')
    sueldo = request.POST.get('sueldo').replace(",",".")
    logo = request.POST["logo"]

   
    #al cargo que capturamos reescribimos sus valores.
    cargoEditar.nombre = nombre
    cargoEditar.funciones = funciones
    cargoEditar.horario = horario
    cargoEditar.requisitos = requisitos
    cargoEditar.sueldo = sueldo
    cargoEditar.logo = logo

    
    #guardamos los datos
    cargoEditar.save()
  
    #enviamosun mensaje de exito dado el caso que haya ocurrido
    messages.success(request, "Cargo actualizado exitosamente.")
   
    return redirect('/')


