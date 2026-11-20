# Mi portafolio

Portafolio personal construido con Django. No utiliza una base de datos persistente; la configuración de SQLite usa memoria y el formulario de contacto abre el cliente de correo del visitante.

## Ejecutar localmente en Windows

Necesitas Python 3.12 o posterior.

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe manage.py runserver
```

Abre <http://127.0.0.1:8000/>. Para detener el servidor, presiona `Ctrl+C`.

## Páginas

- Inicio: `/`
- Sobre mí: `/sobre-mi/`
- Habilidades: `/habilidades/`
- Proyectos: `/proyectos/`
- Detalle de un proyecto: `/proyectos/<slug>/`
- Contacto: `/contacto/`

## CV y contacto

El botón **Descargar CV** entrega el PDF ubicado en `portafolio/static/portafolio/files/`. Ese archivo será público al desplegar el sitio. **Contactar** abre un correo dirigido a `parbrayanjack@gmail.com`; no se envían ni guardan mensajes en el servidor.

## Desplegar gratis en Vercel

Vercel es la opción recomendada para este proyecto: su plan Hobby cuesta $0 y ofrece soporte oficial para aplicaciones Django. El plan tiene límites de uso que pueden cambiar; consúltalos en la [página de precios](https://vercel.com/pricing). A diferencia de Vercel, Netlify no ofrece el mismo flujo directo para ejecutar una aplicación Django WSGI.

1. Asegúrate de que los cambios estén subidos a tu repositorio de GitHub.
2. Crea una cuenta en [Vercel](https://vercel.com/signup), selecciona **Add New → Project** e importa el repositorio `ZeroJack73/mi_portafolio`.
3. Deja como directorio raíz `./`. Vercel detectará Django a partir de `manage.py` y `mi_portafolio/wsgi.py`.
4. En **Environment Variables**, agrega:
   - `DJANGO_SECRET_KEY`: genera un valor privado ejecutando `python -c "import secrets; print(secrets.token_urlsafe(50))"` y pega el resultado en Vercel. No lo guardes en el repositorio.
   - `DJANGO_DEBUG`: `False`.
5. Presiona **Deploy**. Vercel publica el sitio y vuelve a desplegarlo cuando subas cambios a la rama de producción.

La variable `VERCEL_URL` la proporciona Vercel y se añade automáticamente a los hosts permitidos. Si luego conectas un dominio propio, agrega sus nombres de host a `DJANGO_ALLOWED_HOSTS`, separados por comas y sin `https://`.

El archivo `.python-version` selecciona Python 3.14 en Vercel. `STATIC_ROOT` está configurado para que Vercel recopile los recursos de `static/` al desplegar; no hace falta agregar un comando de compilación ni un archivo `vercel.json`.

El sitio no persiste datos. No uses la base SQLite en memoria para guardar información: Vercel ejecuta Django en funciones y no proporciona almacenamiento duradero para esa base.

Más información: [Django en Vercel](https://vercel.com/docs/frameworks/full-stack/django), [versiones de Python compatibles](https://vercel.com/docs/functions/runtimes/python/python-version) y [precios de Vercel](https://vercel.com/pricing).
