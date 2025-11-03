from models.catalogo_modelo import Catalogo, CaracteristicasMovil, CaracteristicasLaptop
from supabase import create_client, Client
from dotenv import load_dotenv
from fastapi import HTTPException
import os 

#---Leer variables de entorno---
load_dotenv()
URL: str = os.getenv('URL')
KEY: str = os.getenv('KEY')

#---Crear cliente de Supabase---
supabase: Client = create_client(URL, KEY)


#---Agregar un nuevo producto al catálogo---
async def agregar_producto(catalogo: Catalogo, 
                           caractMovil: CaracteristicasMovil = None, 
                           caractLaptop: CaracteristicasLaptop = None):

    try: 
        #--Insertar el catálogo y obtener el ID generado--
        catalogo_db = (
            supabase
            .table("catalogo")
            .insert(await crear_diccionarios(catalogo=catalogo, peticion="catalogo"))
            .execute()
        )
        
        #---Obtener el ID del producto insertado---
        catalogo_id = catalogo_db.data[0]["id"]
        
        #---Insertar características según el tipo de dispositivo---
        if caractMovil:
            caracteristicas_db = (
                supabase
                .table("caracteristicas_movil")
                .insert(await crear_diccionarios(catalogo_id=catalogo_id, caractMovil=caractMovil, peticion="caractMovil"))
                .execute()
            )
        elif caractLaptop:
            caracteristicas_db = (
                supabase
                .table("caracteristicas_laptop")
                .insert(await crear_diccionarios(catalogo_id=catalogo_id, caractLaptop=caractLaptop, peticion="caractLaptop"))
                .execute()
            )
        
        return {
            "success": True,
            "catalogo_id": catalogo_id,
            "mensaje": "Producto agregado exitosamente"
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al conectar con la base de datos: {str(e)}") 
       


#---Función para crear los diccionarios de inserción---#
async def crear_diccionarios(catalogo: Catalogo = None,
                             catalogo_id: int = None,
                             caractMovil: CaracteristicasMovil = None, 
                             caractLaptop: CaracteristicasLaptop = None,
                             peticion: str = None
                             ):
    
    if peticion == "catalogo":
        return {
            "nombre" : catalogo.nombre,
            "imagen" : catalogo.imagen,
            "descripcion" : catalogo.descripcion,
            "marca" : catalogo.marca,
            "categoria" : catalogo.categoria,
            "dispositivo" : catalogo.dispositivo,
        }
    
    elif peticion == "caractMovil":
        return {
            "catalogo_id" : catalogo_id,
            "pantalla" : caractMovil.pantalla,
            "procesador" : caractMovil.procesador,
            "memoria_ram" : caractMovil.memoria_ram,
            "almacenamiento" : caractMovil.almacenamiento,
            "camara" : caractMovil.camara,
            "bateria" : caractMovil.bateria,
            "conectividad" : caractMovil.conectividad,
        }
    
    elif peticion == "caractLaptop":
        return {
            "catalogo_id" : catalogo_id,
            "pantalla" : caractLaptop.pantalla,
            "procesador" : caractLaptop.procesador,
            "memoria_ram" : caractLaptop.memoria_ram,
            "almacenamiento" : caractLaptop.almacenamiento,
            "tipo_almacenamiento" : caractLaptop.tipo_almacenamiento,
            "tarjeta_grafica" : caractLaptop.tarjeta_grafica,
            "bateria" : caractLaptop.bateria,
            "conectividad" : caractLaptop.conectividad,
        }
        
    
    