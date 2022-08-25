from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy, reverse
#
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, View,DeleteView
from .models import Favorites
from applications.entrada.models import  Entry

from django.contrib.auth.models import User



class UserPageListView(LoginRequiredMixin, ListView):
    template_name = "favoritos/perfil.html"
    context_object_name='entradas_user'
    login_url=reverse_lazy('users_app:Login')

    def get_queryset(self):

        return Favorites.objects.entradas_user(self.request.user)

class AddFavoritosView(LoginRequiredMixin, View):
    login_url=reverse_lazy('users_app:Login')

    def post(self, request, *args, **kwargs):
        # Recuperar un usuario
        usuario=self.request.user
        entrada=Entry.objects.get(id=self.kwargs['pk'])

        # Registramos Favoritos
        Favorites.objects.create(
            user=usuario,
            entry=entrada,
            add=True,
        )

        return HttpResponseRedirect(
            reverse(
                'favorito_app:Perfil'
            )
        )

class FavoritesDeleteView(DeleteView):
    model = Favorites
    # no necesita el template_name recarga la misma vista
    success_url= reverse_lazy('favorito_app:Perfil')
    
    
def prueba(request):
    favoritos=Favorites.objects.filter(user=request.user.id)
    print(favoritos)
    usuario=request.user.username
    for i in favoritos:
        if i.user.username == usuario:
            # print(i.user.username)
            print('existe')
        else:
            print('no existe')
    return HttpResponse('hola')
