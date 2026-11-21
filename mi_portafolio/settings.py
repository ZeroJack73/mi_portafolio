"""Configuración del proyecto mi_portafolio."""

import os
from pathlib import Path

from django.core.management.utils import get_random_secret_key

BASE_DIR = Path(__file__).resolve().parent.parent

EN_VERCEL = 'VERCEL' in os.environ

# Clave secreta: se toma de la variable de entorno; en Vercel, si no existe,
# se genera una aleatoria para que el despliegue no falle.
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY') or (
    get_random_secret_key() if EN_VERCEL else 'django-insecure-solo-desarrollo-local'
)

# En local se muestra el detalle de errores; en Vercel se usa la página 404 propia.
DEBUG = not EN_VERCEL

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '.vercel.app']

INSTALLED_APPS = [
    'django.contrib.staticfiles',
    'portafolio',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mi_portafolio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'mi_portafolio.wsgi.application'

# El portafolio no guarda datos, así que no usa base de datos.
DATABASES = {}

LANGUAGE_CODE = 'es'
TIME_ZONE = 'America/Guatemala'
USE_I18N = True
USE_TZ = True

# Archivos estáticos (CSS, JS, imágenes y CV).
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
