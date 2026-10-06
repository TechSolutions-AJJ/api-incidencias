# API de incidencias

API para registrar y gestionar incidencias informáticas de la empresa ficticia TechSupport, desarrollada con Python y FastAPI.

## Requisitos
- Python 3
- Git con acceso a GitHub por SSH

## Instalación
```bash
git clone git@github.com:TechSolutions-AJJ/api-incidencias.git
cd api-incidencias
python -m venv .venv
```

Activar el entorno:
- Windows: `.venv\Scripts\activate`
- Linux/macOS: `source .venv/bin/activate`

```bash
pip install -r requirements.txt
```

Crear el archivo `.env` a partir de `.env.example` y rellenar los valores locales.

## Ejecución
```bash
uvicorn app.main:app --reload
```

Documentación interactiva: http://127.0.0.1:8000/docs

## Endpoints
| Método | Ruta | Función |
|---|---|---|
| GET | /incidencias | Listar todas las incidencias |
| GET | /incidencias/{id} | Consultar una incidencia |
| POST | /incidencias | Crear una incidencia |
| PUT | /incidencias/{id} | Modificar una incidencia |
| DELETE | /incidencias/{id} | Eliminar una incidencia |