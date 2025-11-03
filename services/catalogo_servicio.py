from fastapi import HTTPException
from supabase import create_client, Client
from dotenv import load_dotenv
import os 
from models.catalogo_modelo import Catalogo

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



#---Función encargada de retornar el catálogo de productos según los filtros aplicados---#
async def retonar_catalogo(marca: list[str] = [], 
                           categoria: list[str] = [], 
                           precio_min : int | None = None, 
                           precio_max: int | None = None, 
                           ordenar_precio: str | None = None, 
                           ordenar_alfabeticamente: str | None = None, 
                           tipo_dispositivo: str | None = None): 
    
    #--- Verificar si no se aplicaron filtros---#
    if not any([marca, categoria, precio_min, precio_max, ordenar_precio, ordenar_alfabeticamente, tipo_dispositivo]):    
        return await consulta_sin_filtros()     
    return ""
        
        
        
        

###########################################################################################################################################################
# Consultas SQL 
###########################################################################################################################################################

async def consulta_sin_filtros():
    try:
         
        catalogo = (
            supabase
            .table("productos")
            .select("*")
            .execute()
        )
        caracteristicas = (
            supabase
            .table("caracteristicas")
            .select("*")
            .execute()
        )
    except: 
        raise HTTPException(status_code=500, detail="Error al conectar con la base de datos")
        
        

        
        

