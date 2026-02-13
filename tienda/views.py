from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib import messages
from tienda.models import Producto, Cart, CartItem
from django.contrib.auth.decorators import login_required

def catalogo(request):
    # listado catalogo paginado
    productos = Producto.objects.prefetch_related('imagenes').all().order_by('id')
    paginator = Paginator(productos, 10)
    page_number = request.GET.get('page')
    productos = paginator.get_page(page_number)
    agregar_catalogo = {'catalogo': productos}
    return render(request, 'home/catalogo.html', agregar_catalogo)

def detalle_producto(request, producto_id):
    # detalle producto
    producto = get_object_or_404(Producto.objects.prefetch_related('imagenes'), id=producto_id)
    agregar_detalle = {'producto': producto}
    return render(request, 'home/detalle_producto.html', agregar_detalle)

@login_required
def add_to_cart(request, producto_id):
    # agrega producto al carrito
    producto = get_object_or_404(Producto, id=producto_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, producto=producto)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    messages.success(request, f'{producto.nombre} agregado al carrito.')
    return redirect('detalle_producto', producto_id=producto_id)

@login_required
def view_cart(request):
    # carrito y msj whatsapp
    cart, created = Cart.objects.get_or_create(user=request.user)
    items = cart.items.all()
    total = cart.total
    whatsapp_message = "Hola, quiero comprar:\n"
    for item in items:
        whatsapp_message += f"- {item.quantity} x {item.producto.nombre} (₡{item.subtotal})\n"
    whatsapp_message += f"Total: ₡{total}"
    whatsapp_url = f"https://wa.me/50671276909?text={whatsapp_message.replace(' ', '%20').replace('\n', '%0A')}"
    context = {
        'cart': cart,
        'items': items,
        'total': total,
        'whatsapp_url': whatsapp_url,
    }
    return render(request, 'home/cart.html', context)

@login_required
def remove_from_cart(request, item_id):
    # quita item carrito
    item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    item.delete()
    messages.success(request, 'Producto removido del carrito.')
    return redirect('view_cart')