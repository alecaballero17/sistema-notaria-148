from django.contrib import admin
from .models import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre_completo', 'ci', 'telefono', 'fecha_nacimiento')
    search_fields = ('nombre_completo', 'ci')
