from django.shortcuts import render
from tienda.models import Producto
from django.core.paginator import Paginator
from django.db.models import Q

def buscar(request):
    # filtra productos por texto
    query = request.GET.get('q', '')
    productos = Producto.objects.filter(
        Q(nombre__icontains=query) | Q(descripcion__icontains=query)
    ).order_by('id')

    paginator = Paginator(productos, 10)
    page_number = request.GET.get('page')
    productos_page = paginator.get_page(page_number)

    contexto = {
        'query': query,
        'catalogo': productos_page,
        # data pa template busqueda
    }
    return render(request, 'home/search.html', contexto)