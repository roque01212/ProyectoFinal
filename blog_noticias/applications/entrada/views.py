from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView
from applications.entrada.forms import EntryForm
from applications.favoritos.models import Favorites
from .models import Entry, Category
# Create your views here.

class EntryListView(ListView):

    template_name = "entrada/lista.html"
    context_object_name= 'entradas'
    paginate_by=5

    def get_context_data(self, **kwargs):
        context = super(EntryListView, self).get_context_data(**kwargs)
        context['categorias']= Category.objects.all()
        return context
    
    def get_queryset(self):
        kword=self.request.GET.get('kword','')
        categoria=self.request.GET.get('categoria','')
        # consula de busqueda
        resultado=Entry.objects.buscar_entrada(kword, categoria)
        return resultado

class EntryDetailView(DetailView):
    template_name = "entrada/detail.html"
    model = Entry

   
        

def crear_entrada(request):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method=='POST':
            form=EntryForm(request.POST, request.FILES)
            if form.is_valid():
                entrada=form.save(commit=False)
                entrada.user_id=request.user.id
                entrada.save()
                category=form.cleaned_data.get('category'),
                title=form.cleaned_data.get('title'),
                resume=form.cleaned_data.get('resume'),
                content=form.cleaned_data.get('content'),
                image=form.cleaned_data.get('image'),
                return redirect('home_app:Index')
        else:
            form=EntryForm
        return render(request, 'entrada/create.html', {'form':form})
    else:
        return redirect('login')