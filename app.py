from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi_cors import CORS
from database import init_db
from routers import user as user_router
from routers import cars as cars_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield


app = FastAPI(lifespan=lifespan)
CORS(app)

app.include_router(user_router.router, prefix="/users", tags=["Users"])
app.include_router(cars_router.router, prefix="/cars", tags=["Cars"])

@app.get("/", tags=["Root"])
async def read_root() -> dict:
    return {"message": "Welcome to your beanie powered app!"}
