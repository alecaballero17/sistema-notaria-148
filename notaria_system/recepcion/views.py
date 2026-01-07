from django.shortcuts import render
from clientes.models import Cliente
from tramites.models import Tramite

def buscar_cliente(request):
    cliente = None
    tramites = []
    ci = ''

    if request.method == 'POST':
        ci = request.POST.get('ci')
        try:
            cliente = Cliente.objects.get(ci=ci)
            tramites = Tramite.objects.filter(cliente=cliente)
        except Cliente.DoesNotExist:
            cliente = None

    return render(request, 'recepcion/buscar_cliente.html', {
        'cliente': cliente,
        'tramites': tramites,
        'ci': ci
    })
