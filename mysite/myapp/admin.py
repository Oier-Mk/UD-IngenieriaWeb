from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Empresa, Trabajador
# Register your models here.

admin.site.register(Empresa)
admin.site.register(Trabajador)
