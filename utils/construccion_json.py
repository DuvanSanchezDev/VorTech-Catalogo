from typing import List, Dict, Any
from models.catalogo_modelo import Catalogo, CaracteristicasMovil, CaracteristicasLaptop

async def ensamblar_catalogo_con_caracteristicas(
    catalogos: List[Catalogo],
    caracteristicas_moviles: List[CaracteristicasMovil],
    caracteristicas_laptops: List[CaracteristicasLaptop]
) -> Dict[str, List[Dict[str, Any]]]:
    """
    Ensambla el JSON final combinando catálogos con sus características.
    
    Args:
        catalogos: Lista de productos del catálogo
        caracteristicas_moviles: Lista de características de móviles
        caracteristicas_laptops: Lista de características de laptops
    
    Returns:
        Diccionario con la estructura del JSON de respuesta
    """
    
    # Crear diccionarios para búsqueda rápida por catalogo_id
    caracteristicas_moviles_dict = {
        c.catalogo_id: c for c in caracteristicas_moviles
    }
    caracteristicas_laptops_dict = {
        c.catalogo_id: c for c in caracteristicas_laptops
    }
    
    productos = []
    
    for catalogo in catalogos:
        # Estructura base del producto (sin incluir 'dispositivo')
        producto = {
            "id": catalogo.id,
            "nombre": catalogo.nombre,
            "imagen": catalogo.imagen,
            "descripcion": catalogo.descripcion,
            "marca": catalogo.marca,
            "categoria": catalogo.categoria,
            "precio": catalogo.precio,
            "unidades": catalogo.unidades
        }
        
        # Agregar características según el tipo de dispositivo
        if catalogo.dispositivo == "movil" and catalogo.id in caracteristicas_moviles_dict:
            carac = caracteristicas_moviles_dict[catalogo.id]
            producto["caracteristicas"] = {
                "pantalla": carac.pantalla,
                "procesador": carac.procesador,
                "memoria_ram": carac.memoria_ram,
                "almacenamiento": carac.almacenamiento,
                "camara": carac.camara,
                "bateria": carac.bateria,
                "conectividad": carac.conectividad
            }
        
        elif catalogo.dispositivo == "laptop" and catalogo.id in caracteristicas_laptops_dict:
            carac = caracteristicas_laptops_dict[catalogo.id]
            producto["caracteristicas"] = {
                "pantalla": carac.pantalla,
                "procesador": carac.procesador,
                "memoria_ram": carac.memoria_ram,
                "almacenamiento": carac.almacenamiento,
                "tipo_almacenamiento": carac.tipo_almacenamiento,
                "tarjeta_grafica": carac.tarjeta_grafica,
                "bateria": carac.bateria,
                "conectividad": carac.conectividad
            }
        else:
            # Si no hay características o es un tipo desconocido
            producto["caracteristicas"] = {}
        
        productos.append(producto)
    
    return {"productos": productos}