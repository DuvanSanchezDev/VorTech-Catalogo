from fastapi import APIRouter, Depends, HTTPException, Query
from typing import Optional, List
from models.catalogo_modelo import Catalogo, CaracteristicasMovil, CaracteristicasLaptop
from services.agregar_catalogo import agregar_producto
from services.leer_catalogo import retornar_catalogo
from utils.construccion_json import ensamblar_catalogo_con_formato_final

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
async def obtener_catalogo_completo(
    marca: Optional[List[str]] = Query(None),
    categoria: Optional[List[str]] = Query(None),
    precio_min: Optional[int] = None,
    precio_max: Optional[int] = None,
    ordenar_precio: Optional[str] = None, # 'asc' o 'desc'
    ordenar_alfabeticamente: Optional[str] = None, # 'asc' o 'desc'
    tipo_dispositivo: Optional[str] = None
):
    # 1. LLAMADA A LA FUNCIÓN DE CONSULTA (datos crudos y anidados)
    # Esta función ya trae las características de Supabase
    datos_supabase_anidados = await retornar_catalogo(
        marca=marca,
        categoria=categoria,
        precio_min=precio_min,
        precio_max=precio_max,
        ordenar_precio=ordenar_precio,
        ordenar_alfabeticamente=ordenar_alfabeticamente,
        tipo_dispositivo=tipo_dispositivo
    )

    # 2. LLAMADA A LA FUNCIÓN DE ENSAMBLAJE (formato final deseado)
    # Esta función transforma los datos anidados al JSON plano que quieres.
    resultado_json_final = await ensamblar_catalogo_con_formato_final(
        datos_supabase_anidados
    )
    
    # 3. RETORNO DE LA RESPUESTA
    return resultado_json_final


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