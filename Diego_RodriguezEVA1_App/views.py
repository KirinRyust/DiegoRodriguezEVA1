from django.shortcuts import render # type: ignore
import datetime

# Create your views here.
def index(request):
    return render(request, 'templateAPP/index.html')

def renderTemplate(request):
    data ={"nombre":"Diego Alfonso Rodriguez Massa",
           "id":"21039251-3",
           "carrera":"Ingenieria de software",
           "seccion":"AP-77",
           "fecha":datetime.datetime.now()}
    return render(request, 'templateAPP/usuario.html',data)

def electronicos(request):
    data = {"nombre":"Electronicos",
            "foto1":"electronico1.jpg",
            "foto2":"electronico2.jpg",
            "foto3":"electronico3.jpg",
            "electronico1":"Camara Compacta Digital Sony W800", 
            "electronico2":"Impresora Epson EcoTank L121",
            "electronico3":"Microondas Ursus Trotter UT-25 Kromm"}
    return render(request, "templateApp/electronicos.html",data)

def electronico1(request):
    return render(request, "templateApp/electronico1.html")

def electronico2(request):
    return render(request, "templateApp/electronico2.html")

def electronico3(request):
    return render(request, "templateApp/electronico3.html")

def perifericos(request):
    data2 ={"nombre":"Perifericos",
           "foto1":"periferico1.jpg",
           "foto2":"periferico2.jpg",
           "foto3":"periferico3.jpg",
           "periferico1":"Teclado Redragon Vata K580 RGB PRO",
           "periferico2":"Mouse Logitech G502 Hero",
           "periferico3":"Audifonos Redragon Zeus X Wireless"}
    return render(request, "templateApp/perifericos.html", data2)

def periferico1(request):
    return render(request, "templateApp/periferico1.html")

def periferico2(request):
    return render(request, "templateApp/periferico2.html")

def periferico3(request):
    return render(request, "templateApp/periferico3.html")

def accesorios(request):
    data3 = {"nombre":"Accesorios",
            "foto1":"accesorio1.jpg",
            "foto2":"accesorio2.jpg",
            "foto3":"accesorio3.jpg",
            "accesorio1":"",
            "accesorio2":"",
            "accesorio3":""}
    return render(request, "templateApp/accesorios.html", data3)

def accesorio1(request):
    return render(request, "templateApp/accesorio1.html")

def accesorio2(request):
    return render(request, "templateApp/accesorio2.html")

def accesorio3(request):
    return render(request, "templateApp/accesorio3.html")
