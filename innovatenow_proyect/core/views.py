from django.shortcuts import render
from .models import QuienesSomos, Servicio

def home(request):
    # Página estática con información general de la empresa
    return render(request, 'core/base.html')

def quienes_somos(request):
    quienes_somos_info = QuienesSomos.objects.all()
    return render(request, 'core/quienes_somos.html', {'quienes_somos_info': quienes_somos_info})

def servicios(request):
    servicios_info = Servicio.objects.all()
    return render(request, 'core/servicios.html', {'servicios_info': servicios_info})
