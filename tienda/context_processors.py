from tienda.models import Cart

def cart_count(request):
    # cuenta items carrito pa navbar
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        return {'cart_count': cart.items.count()}
    return {'cart_count': 0}