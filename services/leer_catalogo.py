from fastapi import HTTPException
from supabase import create_client, Client
from dotenv import load_dotenv
import os 

"""
Que debo hacer aquí: 
    Crear una función que se encargue de de seleccionar cual es la función más adecuada para realizar el llamado de los  datos a la base de datos de Supbase.

Como debo hacerlo: 
    Para esto, se debe de crear una función que permita analizar cuales de los datos que se le pasaron al endpoint en la catologo_rut.py contienen valores, esto debido a que todos los datos son opcionales.
    Como todos los datos son opcionales, se debe de crear una función que permita identificar cuales de estos datos contienen valores y en base a eso seleccionar la función adecuada para realizar el llamado a la base de datos.
"""

#---Leer variables de entorno---#
load_dotenv()
URL: str = os.getenv('URL')
KEY: str = os.getenv('KEY')

#---Crear cliente de Supabase---#
supabase: Client = create_client(URL, KEY)


async def retornar_catalogo(
    marca: list[str] = [], 
    categoria: list[str] = [], 
    precio_min: int | None = None, 
    precio_max: int | None = None, 
    ordenar_precio: str | None = None, 
    ordenar_alfabeticamente: str | None = None, 
    tipo_dispositivo: str | None = None
): 
    try:
        # Definición de los campos a seleccionar, incluyendo las relaciones anidadas
        select_fields = "*, caracteristicas_movil(*), caracteristicas_laptop(*)"
        
        # 1. Iniciar la consulta
        query = supabase.table("catalogo").select(select_fields)

        # 2. Aplicar filtros condicionalmente
        if marca:
            query = query.in_("marca", marca)
        if categoria:
            query = query.in_("categoria", categoria)
        if precio_min is not None:
            query = query.gte("precio", precio_min)
        if precio_max is not None:
            query = query.lte("precio", precio_max)
        if tipo_dispositivo:
            query = query.eq("dispositivo", tipo_dispositivo)

        # 3. Aplicar ordenamiento condicionalmente (Usando ascending=ascending para claridad)
        if ordenar_precio:
            ascending = ordenar_precio.lower() == 'asc'
            query = query.order("precio", ascending=ascending)
        elif ordenar_alfabeticamente:
            ascending = ordenar_alfabeticamente.lower() == 'asc'
            query = query.order("nombre", ascending=ascending)

        # 4. Ejecutar la consulta final
        response = query.execute()

        # 5. Retornar los datos (Lista de diccionarios con objetos anidados)
        return response.data
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al consultar el catálogo con características: {str(e)}")


        
        

