from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Auto
from .forms import AutoForm

def index(request):
    autos = Auto.objects.all() 
    form = AutoForm() 
    return render(request ,'index.html', {'autos': autos, 'form' : form})

def show(request,auto_id):
    auto = Auto.objects.get(id=auto_id)
    return render(request,'show.html',{'auto': auto})

def post_auto(request):
    form = AutoForm(request.POST)
    if form.is_valid():
        auto = Auto(nombre = form.cleaned_data['nombre'],
                    precio = form.cleaned_data['precio'],
                    color = form.cleaned_data['color'],
                    modelo = form.cleaned_data['modelo'],
                    img_url = form.cleaned_data['img_url'])
        auto.save()
    return HttpResponseRedirect('/')   