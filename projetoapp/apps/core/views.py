from django.shortcuts import render

# Create your views here.
def home(request):
    template_name ='core/base.html'
    context = {}
    return render(request, template_name, context)

def login(request):
    template_name ='core/login.html'
    context = {}
    return render(request, template_name, context)

def filmes(request):
    template_name ='core/filmes.html'
    context = {}
    return render(request, template_name, context)
    
def series(request):
    template_name ='core/series.html'
    context = {}
    return render(request, template_name, context)

def documentarios(request):
    template_name ='core/documentarios.html'
    context = {}
    return render(request, template_name, context) 

def planos(request):
    template_name ='core/planos.html'
    context = {}
    return render(request, template_name, context)   
