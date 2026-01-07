from django.contrib import admin
from .models import Tramite

@admin.register(Tramite)
class TramiteAdmin(admin.ModelAdmin):
    list_display = ('tipo_servicio', 'cliente', 'estado', 'fecha_inicio')
    list_filter = ('estado',)
    search_fields = ('tipo_servicio', 'cliente__nombre_completo', 'cliente__ci')
