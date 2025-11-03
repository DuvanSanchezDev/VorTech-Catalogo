import os 
from jose import JWTError, jwt, ExpiredSignatureError
from models.token_modelo import InformacionToken
from dotenv import load_dotenv

#---Cargar variables de entorno---
load_dotenv()
SECRET_KEY: str = os.getenv("SECRET_KEY")

#---Configuración del algoritmo y tiempo de expiración del token---
ALGORITHM: str = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

#---Verificar y decodificar token de acceso---#
async def verificar_token_acceso(token: str) -> InformacionToken:
    """
    Verifica y decodifica un token de acceso JWT para extraer información del usuario.
    Esta función toma un token JWT como entrada, lo decodifica usando la clave secreta
    configurada y extrae la información del usuario contenida en el payload. Valida
    que todos los campos requeridos estén presentes y retorna un objeto con la
    información del token.
    Args:
        token (str): Token JWT a verificar y decodificar.
    Returns:
        InformacionToken: Objeto que contiene la información extraída del token:
            - id (int): Identificador único del usuario
            - username (str): Nombre de usuario
            - correo (str): Dirección de correo electrónico
            - administrador (bool): Indica si el usuario tiene privilegios de administrador
            - activo (bool): Indica si la cuenta del usuario está activa
    Raises:
        JWTError: Se lanza en los siguientes casos:
            - Token expirado: "Token expirado. Por favor, inicie sesión de nuevo."
            - Token inválido o malformado: "Token de autenticación inválido o malformado."
            - Campos faltantes en el payload del token
    Note:
        Esta función utiliza las constantes globales SECRET_KEY y ALGORITHM
        para la decodificación del token JWT.
    """
    try:
        # Decodificación del token JWT y almacenamiento de la información del usuario
        token_usuario = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id: int = token_usuario.get("id")
        username: str = token_usuario.get("username")
        correo: str = token_usuario.get("correo")
        administrador: bool = token_usuario.get("administrador")
        activo: bool = token_usuario.get("activo")
        
        # Comprobar que la información esencial esté presente
        if id is None or username is None or correo is None or administrador is None or activo is None:
            raise JWTError
        
        # Construcción del modelo con la información del token
        informacion_token = InformacionToken(
            id=id,
            username=username,
            correo=correo,
            administrador=administrador,
            activo=activo
        )
        
        # Retornar la información del token verificado
        return informacion_token
    
    except ExpiredSignatureError:
        # Excepción específica para token expirado
        raise JWTError("Token expirado. Por favor, inicie sesión de nuevo.")
    
    except JWTError:
        # Excepción para token inválido o malformado
        raise JWTError("Token de autenticación inválido o malformado.")
    
#---Validar si es administrador---#
async def verificar_administrador(informacion_token: InformacionToken) -> bool:
    if not informacion_token.administrador:
        return False
    return True


