from pydantic import BaseModel, EmailStr

class InformacionToken(BaseModel):
    id : int 
    username : str 
    correo : EmailStr
    administrador : bool
    activo : bool
