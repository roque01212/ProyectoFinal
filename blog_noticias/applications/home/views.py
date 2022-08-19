from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Suscribers
from .forms import SuscribersForm
# Create your views here.

def inicio(request):
    return render(request, 'home/index.html')


# Suscribers
def form_Suscribers(request):
    if request.method=='POST':
        form=SuscribersForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            suscriptor=info['email']
            suscribers=Suscribers(email=info['email'])
            suscribers.save()
            
            return redirect('/')
    else:
        form=SuscribersForm()
    
    return render(request, 'home/index.html', {"form":form})