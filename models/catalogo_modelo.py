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
    