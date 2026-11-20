from django.http import Http404
from django.shortcuts import render


PROJECTS = [
    {
        'name': 'salud-publica',
        'category': 'salud',
        'title': 'Plataforma de Salud Rural',
        'description': 'Donaciones médicas y suministros para comunidades rurales.',
        'tags': ['Python', 'Web'],
    },
    {
        'name': 'gamekit',
        'category': 'videojuegos',
        'title': 'Gamekit: Arcade Lab',
        'description': 'Juegos interactivos y dinámicas de club universitario.',
        'tags': ['Python', 'Pygame'],
    },
    {
        'name': 'decoder',
        'category': 'seguridad',
        'title': 'Decoder: Cifrado Seguro',
        'description': 'Codificador y decodificador de mensajes con cifrado.',
        'tags': ['Algoritmos', 'CLI'],
    },
]


def inicio(request):
    return render(request, 'portafolio/inicio.html', {'projects': PROJECTS})


def sobre_mi(request):
    return render(request, 'portafolio/sobre_mi.html')


def habilidades(request):
    return render(request, 'portafolio/habilidades.html')


def proyectos(request):
    return render(request, 'portafolio/proyectos.html', {'projects': PROJECTS})


def proyecto_detalle(request, project_name):
    project = next((item for item in PROJECTS if item['name'] == project_name), None)
    if project is None:
        raise Http404('Proyecto no encontrado')

    return render(request, 'portafolio/proyecto_detalle.html', {'project': project})


def contacto(request):
    return render(request, 'portafolio/contacto.html')
