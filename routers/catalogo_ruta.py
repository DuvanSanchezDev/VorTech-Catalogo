from fastapi import APIRouter, Depends, HTTPException
from models.catalogo_modelo import Catalogo, CaracteristicasMovil, CaracteristicasLaptop
from services.agregar_catalogo import agregar_producto 

router = APIRouter(
    prefix="/catalogo",
)

#---Leer la raiz del catalogo---#
@router.get("/")
async def leer_catalogo():
    return {
        "mensaje": "Catálogo de productos"
            }

#---Leer prductos con filtros---#
@router.get("/productos")
async def catalogo(marca: list[str] = [], 
                    categoria: list[str] = [], 
                    precio_min : int | None = None, 
                    precio_max: int | None = None, 
                    ordenar_precio: str | None = None, 
                    ordenar_alfabeticamente: str | None = None, 
                    tipo_dispositivo: str | None = None):
    return "" 


#---Agregar un producto---#    
@router.post("/productos/agregar")
async def agregar_catalogo(catalogo: Catalogo,
                           caractMovil: CaracteristicasMovil = None, 
                           caractLaptop: CaracteristicasLaptop = None):

    respuesta = await agregar_producto(catalogo=catalogo, caractMovil=caractMovil, caractLaptop=caractLaptop)
    return respuesta

#---Actualizar un producto---#
@router.put("/productos/actualizar")
async def actualizar_catalogo():
    return""

#---Eliminar un producto---#
@router.delete("/productos/eliminar")
async def eliminar_catalogo():
    return""