from django.db import models
<<<<<<< HEAD
from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField
from model_utils.models import TimeStampedModel
from .managers import EntryManager
# Create your models here.

class Category(models.Model):
    """Categorias de una entrada"""

    name = models.CharField(
        'Nombre Corto',
        max_length=15,
        unique=True
    )

    class Meta:
        verbose_name='Categoria'
        verbose_name_plural='Categorias'

    def __str__(self):
        return self.name


class Entry(TimeStampedModel):
    """modelo para noticias"""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
       
    )
    
    title = models.CharField(
        'Titulo',
        max_length=200
    )
    resume = models.TextField('Resumen')
    content=RichTextUploadingField('contenido')
    
    image = models.ImageField(
        'Imagen',
        upload_to='Entry',
    )
    objects=EntryManager()

    class Meta:
        verbose_name='Entrada'
        verbose_name_plural='Entradas'

    def __str__(self):
        return  f"{self.title } {self.id}"


=======

# Create your models here.
>>>>>>> Camilo
