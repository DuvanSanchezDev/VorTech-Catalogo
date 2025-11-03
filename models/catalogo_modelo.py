from pydantic import BaseModel

class Catalogo(BaseModel): 
    id: int
    nombre: str
    imagen: str
    descripcion: str
    marca: str 
    categoria: str  
    precio: int | None = None
    unidades: str | None = None
    
class CaracteristicasMovil(BaseModel): 
    id: int
    catalogo_id: int
    pantalla: str 
    procesador: str
    memoria_ram: str
    almacenamiento: str
    camara: str
    bateria: str
    conectividad: str 

class CaracteristicasLaptop(BaseModel):
    id: int
    catalogo_id: int
    pantalla: str 
    procesador: str
    memoria_ram: str
    almacenamiento: str
    tipo_almacenamiento: str 
    tarjeta_grafica: str
    bateria: str
    conectividad: str
    
