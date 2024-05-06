from fastapi import FastAPI

# from app.database import engine  # Assuming database connection logic in database.py
# from app.routers import api  # Assuming API routes are defined in routers/api.py
from .routers import home
from .core.config import settings
from .core import models as models
from .database import engine

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(home.router)
# Include API router


# Basic test route
@app.get("/")
async def base():
    return {"message": f"Hello from the core API! {settings.DATABASE_URL}"}


@app.get("/data")
async def data():
    return {"message": "Data is On and ON"}
