import os
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Modelo, Nivel, Pregunta, Respuesta

class ModeloAdmin(admin.ModelAdmin):
    list_display = ('tipo','nombre')
    search_fields = ('tipo','nombre')
    list_filter = ['tipo']
    
admin.site.register(Modelo, ModeloAdmin)

class NivelAdmin(admin.ModelAdmin):
    list_display = ('numero','nombre','descripcion','ptos_necesarios','modelo')
    search_fields = ('numero','nombre','descripcion','ptos_necesarios','modelo__nombre')
    list_filter = ['modelo','numero']
    
admin.site.register(Nivel, NivelAdmin)

class PreguntaAdmin(admin.ModelAdmin):
    list_display = ('numero','modelo')
    search_fields = ('numero','modelo__nombre')
    list_filter = ['numero','modelo']
    
admin.site.register(Pregunta, PreguntaAdmin)

class RespuestaAdmin(admin.ModelAdmin):
    list_display = ('texto','puntos')
    search_fields = ('texto','puntos')
    list_filter = ['puntos','pregunta__modelo','pregunta__numero']
    
admin.site.register(Respuesta, RespuestaAdmin)