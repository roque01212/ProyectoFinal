from django.urls import path
from .views import login_request,register_request,show_profile, cerrar_sesion
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/',login_request,name='login'),
    path('register/',register_request,name='register'),
    path('logout/', cerrar_sesion, name='logout'),
    path('profile/',show_profile,name='profile'),
    
    ]