# Portafolio personal

Portafolio web desarrollado con Django. Incluye las secciones Inicio, Sobre mí, Habilidades, Proyectos y Contacto.

## Requisitos

- Python 3.12 o posterior.
- PowerShell en Windows.

## Preparar el entorno

Abre PowerShell en la carpeta del proyecto, donde se encuentra `manage.py`, y ejecuta:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install Django==6.1.3
```

Si el comando `python` no está disponible, usa `py -3 -m venv .venv`.

## Comprobar y ejecutar

```powershell
.\.venv\Scripts\python.exe manage.py check
.\.venv\Scripts\python.exe manage.py runserver
```

Abre <http://127.0.0.1:8000/> en el navegador. Para detener el servidor, presiona `Ctrl+C` en la terminal.

## Páginas

- Inicio: `/`
- Sobre mí: `/sobre-mi/`
- Habilidades: `/habilidades/`
- Proyectos: `/proyectos/`
- Detalle de un proyecto: `/proyectos/<slug>/`
- Contacto: `/contacto/`

## Notas

- En desarrollo, Django sirve los recursos estáticos desde `portafolio/static/`.
- La base de datos está configurada como SQLite en memoria; no se crea un archivo persistente y los datos no se conservan al cerrar el proceso.
- El formulario de Contacto y el botón **Solicitar CV** abren el cliente de correo predeterminado. No guardan datos en el sitio.
