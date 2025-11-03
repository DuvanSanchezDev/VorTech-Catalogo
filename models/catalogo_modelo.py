from pydantic import BaseModel

class Catalogo(BaseModel): 
    id: int | None = None  # Opcional, se genera en la BD
    nombre: str
    imagen: str
    descripcion: str
    marca: str 
    categoria: str  
    precio: int | None = None
    unidades: str | None = None
    dispositivo: str 
    
    
class CaracteristicasMovil(BaseModel): 
    id: int | None = None  # Opcional, se genera en la BD
    catalogo_id: int | None = None  # Opcional, se asigna después
    pantalla: str 
    procesador: str
    memoria_ram: str
    almacenamiento: str
    camara: str
    bateria: str
    conectividad: str 

class CaracteristicasLaptop(BaseModel):
    id: int | None = None  # Opcional, se genera en la BD
    catalogo_id: int | None = None  # Opcional, se asigna después
    pantalla: str 
    procesador: str
    memoria_ram: str
    almacenamiento: str
    tipo_almacenamiento: str 
    tarjeta_grafica: str
    bateria: str
    conectividad: str
    
