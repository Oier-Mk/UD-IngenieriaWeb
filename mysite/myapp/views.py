from django.shortcuts import get_object_or_404, get_list_or_404, render

from django.views.generic.detail import *

from django.http import HttpResponse

from django.views.generic.list import *

from .models import *

# Create your views here.

##########LISTED VIEW##########

def index(request): #guarda informacion respecto a la peticion
    return render(request, "index.html")

def nombreEmpresa(request, nombre_empresa): 
    lEmpresas = get_list_or_404(Empresa, nombre = nombre_empresa) #porque sabemos que puede haber mas de una empresa con el mismo nombre
    #devuelve una lista con Modelos empresa
    context = {
        'lEmpresas' : lEmpresas #en el HTML se tiene que usar la variable a la izq
    }
    return render(request,"listaEmpresas.html",context)

def idEmpresa(request, id_empresa): 
    #lEmpleados = get_list_or_404(Trabajador, empresa=id_empresa)
    empresa = get_object_or_404(Empresa, pk=id_empresa) 
    context = {
        'variable' : empresa #en el HTML se tiene que usar la variable a la izq
        #'lVariables' : lEmpleados
    }
    return render(request,"detalleEmpresa.html",context)

'''
def empleados(request): 
    empleados = get_list_or_404(Trabajador)
    context = {
        'lEmpleados' : empleados #en el HTML se tiene que usar la variable a la izq
    }
    return render(request,"listaEmpleados.html",context)
'''

##########DETAILED VIEW##########
class EmpleadoDetailView(DetailView):  #pasa un objeto llamado object que recibe por parametro en el enlace
    model = Trabajador
    template_name = "detalleEmpleado.hmtl"

class EmpleadoListView(ListView):
    model = Trabajador
    queryset = Trabajador.objects.all()
    template_name = "listaEmpleados.html"
    context_object_name = "lEmpleados"
