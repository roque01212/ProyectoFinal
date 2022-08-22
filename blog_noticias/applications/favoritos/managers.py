from genericpath import exists
from django.db import models

class FavoritesManager(models.Manager):

    def entradas_user(self, usuario):
        return self.filter(
            user=usuario
        ).order_by('-created')

    