from fastapi import APIRouter, HTTPException, status
from app.schemas import ProductCreate, ProductRead, ProductUpdate

router = APIRouter(prefix='/api/products', tags='products')

@router.get('/', response_model=list[ProductRead], status_code=status.HTTP_200_OK)
def get_all_product():
    return ['hello']