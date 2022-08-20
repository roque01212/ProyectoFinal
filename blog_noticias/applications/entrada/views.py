from re import TEMPLATE
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Entry

# Create your views here.


class HomePageView(TemplateView):
    template_name = "home/index.html"

    
    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['noticia']=Entry.objects.all()
        return context
    
