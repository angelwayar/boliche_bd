import sys

from fastapi import FastAPI

sys.path.append("..")

from app.features.user.api.routes.user_routes import user_router

app = FastAPI()
app.include_router(user_router)


@app.get("/")
def read_root():
    return {"Hello": "World"}
