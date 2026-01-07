from django.db import models
from clientes.models import Cliente

class Tramite(models.Model):
    ESTADOS = [
        ('REGISTRADO', 'Registrado'),
        ('EN_PROCESO', 'En proceso'),
        ('OBSERVADO', 'Observado'),
        ('FINALIZADO', 'Finalizado'),
        ('ENTREGADO', 'Entregado'),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    tipo_servicio = models.CharField(max_length=100)
    numero_interno = models.CharField(max_length=50)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='REGISTRADO')
    fecha_inicio = models.DateField(auto_now_add=True)
    fecha_entrega_estimada = models.DateField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.tipo_servicio} - {self.cliente}"
