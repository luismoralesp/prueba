from django.contrib import admin
from . import models, forms

"""
Criterios para esta clase:
    Se debe poder listar, editar y eliminar los municipios
"""
class MunicipioAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'nombre', 'estado']
    list_filter = ['codigo', 'nombre', 'estado']
    form = forms.MunicipioForm

"""
Criterios para esta clase:
    - Se debe poder listar, editar y eliminar las regiones. 
    - Al editar una región se debe poder agregar o quitar municipios.
"""
class RegionAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'nombre']
    list_filter = ['codigo', 'nombre']
    form = forms.RegionForm

admin.site.register(models.Municipio, MunicipioAdmin)
admin.site.register(models.Region, RegionAdmin)
