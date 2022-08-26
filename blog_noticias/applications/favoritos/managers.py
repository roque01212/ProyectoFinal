from django.db import models

class FavoritesManager(models.Manager):

    def entradas_user(self, usuario):
        return self.filter(
            user=usuario
        ).order_by('-created')
        
    def favoritos(self, usuario, id_entry):
        # Verificamos si el usuario ya tiene el favorito
        return self.filter(
            user=usuario,
            entry=id_entry
        ).exists()
        
