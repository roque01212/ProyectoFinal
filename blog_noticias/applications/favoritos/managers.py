from django.db import models

class FavoritesManager(models.Manager):

    def entradas_user(self, usuario):
        return self.filter(
            user=usuario
        ).order_by('-created')
        
    def favorito_existente(self, user):
        # favorito_user= self.filter(user=id_user)
        # print(favorito_user)
        # usuario_actual=usuario
        # print(usuario_actual)
        # for i in favorito_user:
        #     if i.user.username == usuario_actual:
        #         return True  
        #     return None

        resultado = self.get(user_id=user)
        print(resultado)
        return resultado