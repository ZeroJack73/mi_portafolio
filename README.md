# Mi portafolio

Portafolio personal de **Brayan Jack Par Tzul**, estudiante del Técnico Universitario
en Informática (UVG, Campus Altiplano), desarrollado con **Django**.

El sitio tiene cinco páginas conectadas por una navegación global (header y footer)
y una página 404 personalizada. No usa base de datos: el contenido está en las
vistas y las plantillas.

---

## Requisitos

| Herramienta | Versión |
|---|---|
| Python | 3.12 o superior |
| Django | 6.1.3 (se instala con `requirements.txt`) |
| Git | Cualquier versión reciente (solo para clonar) |

Para comprobar tu versión de Python:

```bash
python --version
```

---

## Ejecutar el proyecto en local

### 1. Obtener el código

```bash
git clone https://github.com/ZeroJack73/mi_portafolio.git
cd mi_portafolio
```

O descarga el ZIP desde GitHub, descomprímelo y abre una terminal en la carpeta
que contiene `manage.py`.

### 2. Crear y activar el entorno virtual

**Windows (PowerShell):**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

> Si PowerShell bloquea la activación, ejecuta una vez
> `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` y vuelve a intentarlo.

**macOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Cuando el entorno está activo, la terminal muestra `(.venv)` al inicio de la línea.

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Verificar e iniciar el servidor

```bash
python manage.py check
python manage.py runserver
```

### 5. Abrir el sitio

Entra a **<http://127.0.0.1:8000/>** en el navegador.

Para detener el servidor presiona `Ctrl + C` en la terminal.

> No hace falta ejecutar `migrate`: el proyecto no usa base de datos.

---

## Páginas

| Página | Ruta | Contenido |
|---|---|---|
| Inicio | `/` | Hero, foto, frase y accesos a las demás secciones |
| Sobre mí | `/sobre-mi/` | Biografía, formación e intereses |
| Habilidades | `/habilidades/` | Tecnologías por categoría y nivel |
| Proyectos | `/proyectos/` | Tarjetas con filtros en JavaScript y enlaces a cada proyecto |
| Contacto | `/contacto/` | Formulario con validación en JavaScript (no envía datos a un servidor), correo y redes sociales |
| Error 404 | Cualquier ruta no válida | Página personalizada con enlace para volver al inicio |

El botón **Descargar CV** descarga el PDF guardado en los archivos estáticos.

> La página 404 personalizada solo se ve en producción (Vercel). En local,
> Django muestra su página de depuración porque `DEBUG` está activo.

---

## Estructura del proyecto

```text
mi_portafolio/
├── manage.py                  # Comandos de Django (runserver, check...)
├── requirements.txt           # Dependencias (Django)
├── .python-version            # Versión de Python que usa Vercel
├── mi_portafolio/             # Configuración del proyecto
│   ├── settings.py
│   ├── urls.py                # Rutas principales
│   └── wsgi.py                # Punto de entrada del servidor (Vercel)
└── portafolio/                # Aplicación del portafolio
    ├── apps.py
    ├── urls.py                # Rutas de las 5 páginas
    ├── views.py               # Vistas y datos (proyectos, perfil)
    ├── templates/
    │   ├── 404.html
    │   └── portafolio/
    │       ├── base.html      # Header, footer y estructura común
    │       ├── inicio.html
    │       ├── sobre_mi.html
    │       ├── habilidades.html
    │       ├── proyectos.html
    │       └── contacto.html
    └── static/portafolio/
        ├── css/estilos.css
        ├── js/main.js         # Menú móvil, filtros, validación del formulario
        ├── img/               # Foto y portadas de proyectos
        └── files/             # CV en PDF
```

---

## Despliegue en Vercel

1. Sube el repositorio a GitHub.
2. En Vercel, elige **Add New → Project** e importa el repositorio.
3. Vercel detecta Django automáticamente por `manage.py`; no hace falta `vercel.json`.
4. (Recomendado) En **Settings → Environment Variables** agrega `DJANGO_SECRET_KEY`
   con un valor aleatorio y vuelve a desplegar.

Durante el despliegue Vercel instala `requirements.txt`, ejecuta `collectstatic` y
sirve el CSS, el JS, las imágenes y el CV desde su CDN.

---

## Solución de problemas

| Problema | Solución |
|---|---|
| `python` no se reconoce | Instala Python desde python.org y marca *Add Python to PATH*, o usa `py` en lugar de `python`. |
| `No module named django` | Activa el entorno virtual (paso 2) y vuelve a ejecutar `pip install -r requirements.txt`. |
| `Error: That port is already in use` | Usa otro puerto: `python manage.py runserver 8001`. |
| La página se ve sin estilos | Comprueba que ejecutas el comando desde la carpeta que contiene `manage.py`. |
