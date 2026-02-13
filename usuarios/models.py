from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    # modelo de perfil por usuario
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    foto_perfil = models.ImageField(upload_to='perfiles/', blank=True, null=True)

    def __str__(self):
        # texto simple para el perfil
        return f'Perfil de {self.user.username}'
