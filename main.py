from fastapi import FastAPI
from routers import catalogo_ruta

app = FastAPI(
    title="Microservicio de catalogo de la app",
    description="Microservicio encargado de gestionar el catalogo de productos de la aplicacion.",
    version="1.0.0"
)

app.include_router(catalogo_ruta.router)

#---Endpoint para comprobar que el microservicio esta corriendo---
@app.get("/")
async def leer_raiz():
    return {
        "mensaje": "Bienvenido al microservicio de catalogo de la app"
        }
