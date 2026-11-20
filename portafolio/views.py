from django.shortcuts import render


PROJECTS = [
    {
        'name': 'salud-publica',
        'category': 'salud',
        'label': 'Salud · Impacto',
        'title': 'Plataforma de Salud Rural',
        'description': 'Donaciones médicas y suministros para comunidades rurales.',
        'tags': ['Python', 'Web'],
    },
    {
        'name': 'gamekit',
        'category': 'videojuegos',
        'label': 'Comunidad · Gamedev',
        'title': 'Gamekit: Arcade Lab',
        'description': 'Juegos interactivos y dinámicas de club universitario.',
        'tags': ['Python', 'Pygame'],
    },
    {
        'name': 'decoder',
        'category': 'seguridad',
        'label': 'Seguridad · Cripto',
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


def contacto(request):
    return render(request, 'portafolio/contacto.html')
