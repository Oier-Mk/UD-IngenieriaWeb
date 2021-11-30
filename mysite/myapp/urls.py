from django.urls import path

from django.views.generic.detail import DetailView

from . import views

from .views import *

urlpatterns = [
    # myApp
    path('', views.index, name='index'), #como es una vista home ho es necesario cargar ningun indice
    # myApp/[nombreEmpresa]
    path('<str:nombre_empresa>/', views.nombreEmpresa, name='nombre'), #con nombre de la empresa
    # myApp/empresa/[id]
    path('empresas/<int:id_empresa>', views.idEmpresa, name='id'), #con id de empresa
    # myApp/empleados/listado
    path('empleados/listado', EmpleadoListView.as_view(), name='empleados'), 
    # myApp/empleado/[pk]
    path('detail/empleado/<int:pk>', EmpleadoDetailView.as_view(), name='detalle'),
]   


#id es el atributo de un objeto 
#un pk es un campo generico que quiero que sea el primary key