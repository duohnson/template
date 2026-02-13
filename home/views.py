from django.shortcuts import render

def index(request):
    # home pricipal con ofertas
    from tienda.models import Producto
    ofertas = Producto.objects.prefetch_related('imagenes').filter(is_oferta=True)
    return render(request, 'home/index.html', {'ofertas': ofertas})

def contacto(request):
    # pagina contacto
    return render(request, 'home/contacto.html')

def tienda(request):
    # plantilla tienda
    return render(request, 'home/tienda.html')