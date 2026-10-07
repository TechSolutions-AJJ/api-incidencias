import os
from dotenv import load_dotenv
from fastapi import FastAPI, Header, HTTPException, status
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


@app.get("/incidencias/{incidencia_id}", response_model=Incidencia)
def consultar_incidencia(incidencia_id: int):
    for incidencia in incidencias:
        if incidencia.id == incidencia_id:
            return incidencia
    raise HTTPException(status_code=404, detail="Incidencia no encontrada")


@app.post("/incidencias", response_model=Incidencia, status_code=status.HTTP_201_CREATED)
def crear_incidencia(datos: IncidenciaBase):
    nueva = Incidencia(id=next(generador_id), **datos.model_dump())
    incidencias.append(nueva)
    return nueva

@app.put("/incidencias/{incidencia_id}", response_model=Incidencia)
def modificar_incidencia(incidencia_id: int, datos: IncidenciaBase):
    for posicion, incidencia in enumerate(incidencias):
        if incidencia.id == incidencia_id:
            actualizada = Incidencia(id=incidencia_id, **datos.model_dump())
            incidencias[posicion] = actualizada
            return actualizada
    raise HTTPException(status_code=404, detail="Incidencia no encontrada")


@app.delete("/incidencias/{incidencia_id}")
def eliminar_incidencia(incidencia_id: int, x_admin_token: str = Header(default=None)):
    admin_token = os.getenv("ADMIN_TOKEN")
    if not admin_token or x_admin_token != admin_token:
        raise HTTPException(status_code=403, detail="Token de administración no válido")
    for posicion, incidencia in enumerate(incidencias):
        if incidencia.id == incidencia_id:
            incidencias.pop(posicion)
            return {"mensaje": "Incidencia eliminada"}
    raise HTTPException(status_code=404, detail="Incidencia no encontrada")
