from django.db import models

class Cliente(models.Model):
    nombre_completo = models.CharField(max_length=150)
    ci = models.CharField(max_length=20, unique=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre_completo} - {self.ci}"
