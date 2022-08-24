from django.db import models
from django.conf import settings

# Create your models here.
class User_profile(models.Model):
    """Model definition for MODELNAME."""
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='profile')
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=200, blank=True)
    email = models.CharField(max_length=100)
    image = models.ImageField(upload_to = 'About/', blank=True)

    class Meta:
        """Meta definition for MODELNAME."""

        verbose_name = 'Perfil de Usuario'
        verbose_name_plural = 'Perfiles de Usuarios'

    def __str__(self):

        return self.user.username + ' - profile'
       

    


        """Unicode representation of MODELNAME."""
        return (f" {self.user.username } {self.id}")


