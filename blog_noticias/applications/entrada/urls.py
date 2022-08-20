from django.urls import path
from . import views

app_name='entrada_app'

urlpatterns = [
    path(
        'noticia/', 
        views.HomePageView.as_view(), 
        name='Noticia'
    ),

] 
