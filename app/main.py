import sys

from fastapi import FastAPI

sys.path.append("..")

from app.features.user.api.routes.user_routes import user_router
from app.features.club.api.routes.club_routes import club_router

app = FastAPI()
app.include_router(user_router)
app.include_router(club_router)


@app.get("/")
def read_root():
    return {"Hello": "World"}
