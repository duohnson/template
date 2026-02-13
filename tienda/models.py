from django.db import models
from django.contrib.auth.models import User

# creacion de prods dinamica

class Producto(models.Model):
    # modelo producto
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=0)
    descripcion = models.TextField()
    is_oferta = models.BooleanField(default=False)

    def __str__(self):
        # texto pa admin y debug
        return self.nombre

    @property
    def primera_imagen(self):
        # primer imagen si hay
        return self.imagenes.first()

class ProductImage(models.Model):
    # imagenes del producto
    producto = models.ForeignKey(Producto, related_name='imagenes', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='productos/')

    def __str__(self):
        # nombre pa mostrar
        return f"Imagen de {self.producto.nombre}"

class Cart(models.Model):
    # carrito del user
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # etiqueta carrito
        return f"Carrito de {self.user.username}"

    @property
    def total(self):
        # total carrito
        return sum(item.subtotal for item in self.items.all())

class CartItem(models.Model):
    # item del carrito
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        # texto item
        return f"{self.quantity} x {self.producto.nombre}"

    @property
    def subtotal(self):
        # subtotal por item
        return self.producto.precio * self.quantity