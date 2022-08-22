from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth import login,logout,authenticate
from .models import Users

from .forms import User_registrations_form


def login_request(request):
    if request.method == 'POST':
        form =AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                
                context = {'message':f'Bienvenido {username}!!'}
                return render(request, 'home/index.html', context = context)
        form =  AuthenticationForm()
        return render(request, 'users/login.html', {'error': 'Formulario invalido', 'form':form})
    elif request.method == 'GET':
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form':form})

def register_request(request):
    if request.method == 'POST':
        form =  User_registrations_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            context = {'errors':form.errors}
            form = User_registrations_form()
            context['form'] = form
            return render(request,'users/register.html',{'form': form})

    elif request.method == 'GET':
        form = User_registrations_form()
        return render(request,'users/register.html',{'form': form})


def show_profile(request):
    if request.user.is_authenticated:
       
        return render(request,'users/profile.html')


# def show_profile(request):
#     if request.user.is_authenticated:
#         return HttpResponse(request.user)

