from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.views.generic import UpdateView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .models import User_profile
from .forms import User_registrations_form, UserForm


def login_request(request):
    if request.method == 'POST':
        form =AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                
                
                return redirect('home_app:Index')
        form =  AuthenticationForm()
        return render(request, 'users/login.html', {'error': 'Formulario invalido', 'form':form})
    elif request.method == 'GET':
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form':form})

def register_request(request):
    if request.method == 'POST':
        form =  User_registrations_form(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            error =form.errors
            form = User_registrations_form()
            
            return render(request,'users/register.html',{'form': form ,'error':error})

    elif request.method == 'GET':
        form = User_registrations_form()
        return render(request,'users/register.html',{'form': form})


def cerrar_sesion(request):
    logout(request)
    return redirect("home_app:Index")


class RegistarUsuario(FormView):
    template_name='users/profile.html'
    form_class=UserForm
    # se recarga la misma vista
    success_url=reverse_lazy('favorito_app:Perfil')

    def form_valid(self, form):

        usuario=User_profile(
            user=self.request.user,
            phone=form.cleaned_data['phone'],
            address=form.cleaned_data['address'],
            email=form.cleaned_data['email'],
            image=form.cleaned_data['image'],
        )
        usuario.save()
        return super(RegistarUsuario, self).form_valid(form)


class UpdateUser(UpdateView):
    model = User_profile
    template_name='users/update.html'
    fields=(
        'phone',
        'address',
        'email',
        'image',
    )
    success_url =  reverse_lazy('home_app:Index')
    def form_valid(self, form) :

        return super(UpdateUser,self).form_valid(form)



