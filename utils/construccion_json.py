from typing import List, Dict, Any

# Nota: Ya no necesitamos los modelos CaracteristicasMovil/Laptop aquí, solo Catalogo
# La entrada son los diccionarios crudos de Supabase

async def ensamblar_catalogo_con_formato_final(
    datos_supabase_anidados: List[Dict[str, Any]]
) -> Dict[str, List[Dict[str, Any]]]:
    """
    Transforma la estructura anidada de Supabase a un formato JSON plano 
    con las características consolidadas.
    
    Args:
        datos_supabase_anidados: Lista de diccionarios devueltos directamente por retornar_catalogo.
    
    Returns:
        Diccionario con la estructura del JSON de respuesta {"productos": [...]}.
    """
    
    productos_finales = []
    
    for item in datos_supabase_anidados:
        # 1. Crear la estructura base del producto (copiando todos los campos)
        producto = item.copy()
        
        # 2. Inicializar el diccionario de características
        caracteristicas = {}
        
        # 3. Consolidar las características del móvil
        moviles_data = producto.pop("caracteristicas_movil", None)
        if moviles_data and isinstance(moviles_data, dict):
            # Usamos update para mover todos los pares clave-valor (excepto id/catalogo_id)
            for k, v in moviles_data.items():
                if k not in ["id", "catalogo_id"]:
                    caracteristicas[k] = v
        
        # 4. Consolidar las características del laptop (si no es móvil)
        laptops_data = producto.pop("caracteristicas_laptop", None)
        if laptops_data and isinstance(laptops_data, dict):
            # Usamos update para mover todos los pares clave-valor (excepto id/catalogo_id)
            for k, v in laptops_data.items():
                if k not in ["id", "catalogo_id"]:
                    caracteristicas[k] = v

        # 5. Insertar las características consolidadas en el producto final
        producto["caracteristicas"] = caracteristicas
        
        # 6. (Opcional) Limpiar cualquier otro campo que no necesites en la raíz (ej. catalogo_id)
        producto.pop("catalogo_id", None)
        
        productos_finales.append(producto)
    
    return {"productos": productos_finales}