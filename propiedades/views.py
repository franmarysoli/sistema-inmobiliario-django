from django.shortcuts import render, get_object_or_404
from .models import Propiedad, TipoPropiedad

# Create your views here.

def lista_propiedades(request):
    """Vista para mostrar el listado de todas las propiedades disponibles"""
    propiedades = Propiedad.objects.all()
    tipos = TipoPropiedad.objects.all()
    
    # Filtros opcionales
    tipo_filtro = request.GET.get('tipo')
    estado_filtro = request.GET.get('estado')
    
    if tipo_filtro:
        propiedades = propiedades.filter(tipo__id=tipo_filtro)
    
    if estado_filtro:
        propiedades = propiedades.filter(estado=estado_filtro)
    
    context = {
        'propiedades': propiedades,
        'tipos': tipos,
        'tipo_seleccionado': tipo_filtro,
        'estado_seleccionado': estado_filtro,
    }
    
    return render(request, 'propiedades/lista_propiedades.html', context)


def detalle_propiedad(request, pk):
    """Vista para mostrar el detalle de una propiedad específica"""
    propiedad = get_object_or_404(Propiedad, pk=pk)
    
    context = {
        'propiedad': propiedad,
    }
    
    return render(request, 'propiedades/detalle_propiedad.html', context)
