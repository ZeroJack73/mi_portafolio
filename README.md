# Mi portafolio

Portafolio personal desarrollado con Django. Usa SQLite en memoria, así que no conserva datos al cerrar el proceso.

## Requisitos

- Python 3.12 o posterior.
- PowerShell en Windows.

## Ejecutar localmente

Abre PowerShell en la carpeta donde está `manage.py` y ejecuta:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install Django==6.1.3
.\.venv\Scripts\python.exe manage.py check
.\.venv\Scripts\python.exe manage.py runserver
```

Visita <http://127.0.0.1:8000/>. Para detener el servidor, presiona `Ctrl+C`.

## Páginas

- Inicio: `/`
- Sobre mí: `/sobre-mi/`
- Habilidades: `/habilidades/`
- Proyectos: `/proyectos/`
- Contacto: `/contacto/`

El botón **Descargar CV** entrega el PDF desde los archivos estáticos. **Contactar** abre el cliente de correo; el sitio no guarda mensajes.
