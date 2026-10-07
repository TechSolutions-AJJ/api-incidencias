import os
from dotenv import load_dotenv
from fastapi import FastAPI, status
from pydantic import BaseModel
from itertools import count

load_dotenv()

app = FastAPI(title=os.getenv("APP_NAME", "API de incidencias"))


class IncidenciaBase(BaseModel):
    titulo: str
    descripcion: str
    estado: str = "abierta"
    prioridad: str = "media"
    tecnico: str


class Incidencia(IncidenciaBase):
    id: int


# Almacenamiento en memoria (el PDF no pide base de datos)
incidencias: list[Incidencia] = [
    Incidencia(
        id=1,
        titulo="No arranca el ordenador 12",
        descripcion="El equipo no muestra imagen",
        estado="abierta",
        prioridad="alta",
        tecnico="Ana",
    )
]

generador_id = count(2)


@app.get("/")
def inicio():
    return {"mensaje": "API de incidencias operativa"}


@app.get("/incidencias", response_model=list[Incidencia])
def listar_incidencias():
    return incidencias

@app.post("/incidencias", response_model=Incidencia, status_code=status.HTTP_201_CREATED)
def crear_incidencia(datos: IncidenciaBase):
    nueva = Incidencia(id=next(generador_id), **datos.model_dump())
    incidencias.append(nueva)
    return nueva