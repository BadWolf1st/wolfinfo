from fastapi import FastAPI, Response
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache
from fastapi.middleware.cors import CORSMiddleware

from redis import asyncio as aioredis
from starlette import status

from src.libs.config import Config
from src.mode import MODE

from src.req.auth.base_config import auth_backend, fastapi_users
from src.req.auth.schemas import UserRead, UserCreate

from src.req.main_inf.router import router as router_main_inf

from src.req.images.router import router as router_images

cfg = Config(MODE)

app = FastAPI(
    debug=True if MODE == "DEV" else False, # debug only in devmode
    title="WolfInfo.ru v5 - API Service"
)

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", status_code=status.HTTP_421_MISDIRECTED_REQUEST)
def read_root():
    return Response(status_code=status.HTTP_421_MISDIRECTED_REQUEST)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(router_main_inf)
app.include_router(router_images)


@app.on_event("startup")
async def startup_event() -> None:
    redis = aioredis.from_url(f"redis://{cfg.REDIS_HOST}:6379", encoding="utf-8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
