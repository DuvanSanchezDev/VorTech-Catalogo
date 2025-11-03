from fastapi import APIRouter, Depends, HTTPException

router = APIRouter(
    prefix="/catalogo",
)

@router.get("/")
async def leer_catalogo():
    return {
        "mensaje": "Catálogo de productos"
            }

