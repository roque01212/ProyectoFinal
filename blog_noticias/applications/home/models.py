from django.db import models
# app terceros
# Create your models here.

class About(models.Model):
    """Modelo sobre nosotros."""

    full_name = models.CharField(
        'Nombre completo',
        max_length=30
    )
    last_name = models.CharField(
        'Apellido',
        max_length=30
    )
    image = models.ImageField(
        'Foto',
        upload_to='About',
    )
    date_birth = models.DateField(
        'fecha Nacimiento',
        blank=True,
        null=True
    )
    age = models.PositiveSmallIntegerField()
    email = models.EmailField()
    phone = models.CharField(
        'Telefono',
        max_length=20
    )
    description = models.TextField()

    

    class Meta:
        """Meta definition for MODELNAME."""

        verbose_name = 'Informacion Personal'
        verbose_name_plural = 'Sobre Nosotros'

    def __str__(self):
        return f"{self.full_name} - {self.last_name} - {self.email} "


class Suscribers(models.Model):
    """ Suscripciones """
    email = models.EmailField()

    class Meta:
        """Meta definition for Suscribers."""

        verbose_name = 'Suscriptor'
        verbose_name_plural = 'Suscriptores'

    def __str__(self):
        return self.email

class Contact(models.Model):
    """Formulario Contacto."""
    
    full_name = models.CharField(
        'Nombres',
        max_length=50
    )
    email = models.EmailField()
    messagge = models.TextField()

    class Meta:
        """Meta definition for Contact."""

        verbose_name = 'Contacto'
        verbose_name_plural = 'Mensajes'

    def __str__(self): 
        return self.full_name        
