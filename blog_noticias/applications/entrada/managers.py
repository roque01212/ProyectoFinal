from django.db import models

class EntryManager(models.Manager):
    """ porcedimiento para entrada """

    def buscar_entrada(self, kword, categoria):
        # procedimiento para buscar entradas por categoria o palabra clave
        if len(categoria)> 0:
            return self.filter(
                category__name=categoria,
                title__icontains=kword,
            ).order_by('-created')
        else:
            return self.filter(
                title__icontains=kword,  
            ).order_by('-created')
