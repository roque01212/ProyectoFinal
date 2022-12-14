
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView
from .models import Contact, Suscribers, About
from .forms import SuscribersForm, ContactForm
from applications.entrada.models import  Entry
# Create your views here.

class HomePageView(TemplateView):
    template_name = "home/index.html"

    
    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['noticia']=Entry.objects.first()
        context['categorias']=Entry.objects.all().order_by('-created')[:4]
        
        context['ultimas_noticias']=Entry.objects.order_by('created')[:6]
        return context
    

# Suscribers
def form_Suscribers(request):
    if request.method=='POST':
        form=SuscribersForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            suscribers=Suscribers(email=info['email'])
            suscribers.save()
            return HttpResponseRedirect(reverse('home_app:Index'))

    return render(request, 'home/index.html', )


def form_contact(request):
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            print(info)
            contact=Contact(full_name=info['full_name'], email=info['email'], messagge=info['messagge'])
            contact.save()
            
            return HttpResponseRedirect(reverse('home_app:Index'))
    
    
    return render(request, 'home/index.html') 

def about(request):
    about=About.objects.all()
    return render(request, 'home/about.html', {'about':about})

# Create your views here.

def inicio(request):
    return render(request, 'home/index.html')



def ListMessaggeAndSubs(request):
    if request.user.is_authenticated and request.user.is_superuser:
        listmessage = Contact.objects.all()
        subscription = Suscribers.objects.all()
        subscriptionTodal =subscription.count()
        context= {
            'listmessagge': listmessage,
            'subscription':subscription,
            'subscriptionTodal':subscriptionTodal,
        }
        return render(request,'home/messaggeAndSubs.html',context=context)
    return redirect('login')