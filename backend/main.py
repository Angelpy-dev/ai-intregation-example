from fastapi import FastAPI
from api.routes import router


app = FastAPI(
    title="Simple AI Agent"
)


app.include_router(
    router,
    prefix="/api"
)
