from django.shortcuts import render


def inicio(request):
    return render(request, 'portafolio/inicio.html')


def sobre_mi(request):
    return render(request, 'portafolio/sobre_mi.html')


def habilidades(request):
    return render(request, 'portafolio/habilidades.html')


def proyectos(request):
    return render(request, 'portafolio/proyectos.html')


def contacto(request):
    return render(request, 'portafolio/contacto.html')
