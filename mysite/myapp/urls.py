from django.urls import path

from django.views.generic.detail import DetailView

from . import views

urlpatterns = [
    # myApp
    path('', views.index, name='index'), #como es una vista home ho es necesario cargar ningun indice
    # myApp/[nombreEmpresa]
    path('<str:nombre_empresa>/', views.nombreEmpresa, name='nombre'), #con nombre de la empresa
    # myApp/empresa/[id]
    path('empresas/<int:id_empresa>', views.idEmpresa, name='id'), #con id de empresa
    # myApp/empleados
    path('empleados/listado', views.empleados, name='empleados'), 
    # myApp/
    path('detail/empleado/<int:pk>', DetailView.as_view(), name='detalle'),
]   


#id es el atributo de un objeto 
#un pk es un campo generico que quiero que sea el primary key