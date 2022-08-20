from django.urls import path
from . import views

app_name='home_app'

urlpatterns = [
    path(
        '', 
        views.HomePageView.as_view(), 
        name='Index'
    ),
    path(
        'register-suscription/', 
        views.form_Suscribers,
        name='Register',
    ),
    path(
        'contact/', 
        views.form_contact,
        name='Contact',
    ), 
    path(
        'about/', 
        views.about,
        name='About',
    ),
] 
