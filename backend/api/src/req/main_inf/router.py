from fastapi import APIRouter, Depends, HTTPException, Response, status
from fastapi_cache import JsonCoder
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi_cache.decorator import cache

# from .models import lenta, company
# from .schemas import Lenta, Company
from src.database import get_async_session

router = APIRouter(
    prefix="/main-info",
    tags=["Main information"]
)

@router.get("/site-logo")
@cache(expire=3600)
async def get_site_logo(session: AsyncSession = Depends(get_async_session)):
	...