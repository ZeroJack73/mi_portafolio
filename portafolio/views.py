from django.shortcuts import render


PROJECTS = [
    {
        'name': 'salud-publica',
        'category': 'salud',
        'title': 'Salud Pública',
        'description': 'Orientación y servicios de salud para San Lucas Tolimán, con información preventiva, directorio médico y preconsulta digital.',
        'tags': ['Prevención', 'Servicios web'],
        'url': 'https://zerojack73.github.io/Salud-publica/#view-inicio',
    },
    {
        'name': 'ruta-equidad',
        'category': 'educacion',
        'title': 'La Ruta de la Equidad',
        'description': 'Aventura de plataformas por tres comunidades que integra seis decisiones para aprender sobre equidad.',
        'tags': ['Videojuego', 'Educación', 'Equidad'],
        'url': 'https://gleeful-eclair-a9b7b4.netlify.app/',
    },
    {
        'name': 'colua-digital',
        'category': 'cooperativa',
        'title': 'Colua Digital',
        'description': 'Portal web para asociados de COLUA MICOOPE, con simuladores de crédito y ahorro, servicios financieros y canales de atención.',
        'tags': ['Portal web', 'Simuladores', 'Prácticas'],
        'url': 'https://coluarl.github.io/Colua-Web/web/',
    },
]

PROFILE = {
    'name': 'Brayan Jack Par Tzul',
    'program': 'Técnico Universitario en Informática',
    'faculty': 'Facultad de Ingeniería',
    'university': 'Universidad del Valle de Guatemala',
    'university_short': 'UVG',
    'campus': 'Campus Altiplano',
    'study_status': 'En curso',
    'formation_status': 'Formación actual',
}


def inicio(request):
    return render(request, 'portafolio/inicio.html', {'projects': PROJECTS})


def sobre_mi(request):
    return render(request, 'portafolio/sobre_mi.html', {'profile': PROFILE})


def habilidades(request):
    return render(request, 'portafolio/habilidades.html', {
        'skills_intro': 'Stack técnico enfocado en Python, Django y desarrollo web robusto.',
    })


def proyectos(request):
    return render(request, 'portafolio/proyectos.html', {'projects': PROJECTS})


def contacto(request):
    return render(request, 'portafolio/contacto.html', {
        'contact_email': 'parbrayanjack@gmail.com',
    })
