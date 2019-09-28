from django.shortcuts import render
#from django.http import HttpResponse
# Create your views here.
def index(request):
    
   # return HttpResponse("<h1>Bienvenido a Automart</h1>"
    #nombre = "VW jetta"
    #precio = 145000
    #modelo = 2018
    #color = "rojo"

    #contexto = {'Auto_nombre' : nombre,
    #'Auto_modelo': modelo,
    # 'Auto_precio': precio,
    # 'Auto_color': color}
     
    return render(request ,'index.html', {'autos': autos})

class Auto:
    def __init__(self, nombre, modelo, precio, color, img_url):
        self.nombre = nombre
        self.modelo = modelo
        self.precio = precio
        self.color = color
        self.img_url = img_url
        
autos = [ Auto("VW jetta", 2018, 145000, "rojo", "https://img.motoryracing.com/noticias/portada/23000/23731-n.jpg"),
            Auto("Batimovil", 2012, 14000000, "negro mate", "https://img.motoryracing.com/noticias/portada/23000/23731-n.jpg"),
            Auto("Tesla Model S", 2018, 12000000, "rojo","https://img.motoryracing.com/noticias/portada/23000/23731-n.jpg"),
            Auto("Delorean", 1985, 0, "plata", "https://img.motoryracing.com/noticias/portada/23000/23731-n.jpg")]