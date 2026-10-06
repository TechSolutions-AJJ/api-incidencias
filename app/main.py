import os
from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()
app = FastAPI(title=os.getenv("APP_NAME", "API de incidencias"))

@app.get("/")
def inicio():
    return {"mensaje": "API de incidencias operativa"}