from django.shortcuts import render

usuarios = [
    {
        'nombre' : "Juan",
        'apellido' : "Perez",
        'edad' : "35",
        'mail' : "juan.perez@example.com",
        'telefono' : "1234567890"
    },
    {
        'nombre' : "María",
        'apellido' : "Lopez",
        'edad' : "28",
        'mail' : "maria.lopez@example.com",
        'telefono' : "9876543210"
    },
    {
        'nombre' : "Laura",
        'apellido' : "Ramirez",
        'edad' : "31",
        'mail' : "laura.ramirez@example.com",
        'telefono' : "7890123456"
    },
    {
        'nombre' : "Carlos",
        'apellido' : "Sanchez",
        'edad' : "42",
        'mail' : "carlos.sanchez@example.com",
        'telefono' : "4567890123"
    },
    {
        'nombre' : "Pedro",
        'apellido' : "Gonzalez",
        'edad' : "39",
        'mail' : "pedro.gonzalez@example.com",
        'telefono' : "3210987654"
    },
]


# Create your views here.
def index(request):
   
    return render(request, 'appTelovendo/index.html')


def clientes(request):
    auxiliar = {
        'usuarios' : usuarios
    }
    return render(request, 'appTelovendo/clientes.html', auxiliar)