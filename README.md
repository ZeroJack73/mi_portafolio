# Mi portafolio

Portafolio personal desarrollado con Django. Usa SQLite en memoria, así que no conserva datos al cerrar el proceso.

## Requisitos

- Python 3.12 o posterior.
- PowerShell en Windows.

## Ejecutar localmente

Abre PowerShell en la carpeta donde está `manage.py` y ejecuta:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe manage.py check
.\.venv\Scripts\python.exe manage.py runserver
```

Visita <http://127.0.0.1:8000/>. Para detener el servidor, presiona `Ctrl+C`.

## Desplegar en Vercel

Importa el repositorio en Vercel y confirma que **Root Directory** sea la carpeta
que contiene `manage.py`. Vercel detecta Django desde `manage.py` y sus
dependencias en `requirements.txt`; no necesita un `index.html` ni una regla
manual de `builds`/`routes`.

En **Settings > Environment Variables**, agrega `DJANGO_SECRET_KEY` con un valor
aleatorio y vuelve a desplegar. Para usar un dominio personalizado, agrega
también `DJANGO_ALLOWED_HOSTS` con los dominios separados por comas. Vercel
agrega automáticamente los dominios de sus despliegues. Los archivos estáticos
se recopilan durante el build usando `STATIC_ROOT`.

## Páginas

- Inicio: `/`
- Sobre mí: `/sobre-mi/`
- Habilidades: `/habilidades/`
- Proyectos: `/proyectos/`
- Contacto: `/contacto/`

El botón **Descargar CV** entrega el PDF desde los archivos estáticos. **Contactar** abre el cliente de correo; el sitio no guarda mensajes.
