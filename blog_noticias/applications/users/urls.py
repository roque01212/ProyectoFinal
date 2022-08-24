
from django.urls import path
from .views import  RegistarUsuario, UpdateUser, login_request,register_request, cerrar_sesion



urlpatterns = [
    path('login/',login_request,name='login'),
    path('register/',register_request,name='register'),
    path('logout/', cerrar_sesion, name='logout'),
    path('profile/', RegistarUsuario.as_view(), name='Profile'),
    path('update/<pk>/', UpdateUser.as_view(), name='Update'),
    
    
    ]