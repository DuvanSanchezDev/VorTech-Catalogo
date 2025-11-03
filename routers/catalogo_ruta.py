from fastapi import APIRouter, Depends, HTTPException

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
async def productos(marca: list[str] = [], categoria: list[str] = [], precio_min : int | None = None, precio_max: int | None = None, ordenar_precio: str | None = None):
    return "" 

#---Agregar un producto---#    
@router.post("/productos/agregar")
async def agregar_producto():
    return""

#---Actualizar un producto---#
@router.put("/productos/actualizar")
async def actualizar_producto():
    return""

#---Eliminar un producto---#
@router.delete("/productos/eliminar")
async def eliminar_producto():
    return""