from django.urls import path
from . import views

app_name='home_app'

urlpatterns = [
    path(
        '', 
        views.inicio, 
        name='Index'
    ),
    path(
        'register-suscription/', 
        views.form_Suscribers,
        name='Register',
    ), 
] 
