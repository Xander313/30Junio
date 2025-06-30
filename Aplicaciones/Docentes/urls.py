#configuracion de rutas especificas de la aplicacion de empresas


from django.urls import path

from . import views 

urlpatterns = [
    path('', views.inicio),
    path('nuevoCargo/', views.nuevoCargo),
    path('guardarCargo/', views.guardarCargo),
    path('eliminarCargo/<id>', views.eliminarDatosPorId),
    path('editarCargo/<id>', views.editarCargo),
    path('procesarEdicionCargo/<id>', views.editarCargoEjecucion, name='procesarEdicionCargo'),


]


