# https://fastapi.tiangolo.com/#create-it
from fastapi import FastAPI

app = FastAPI()

async def hello_world(*args, **kwargs):
    return {"Hello": "World"}

app.get("/")(hello_world)
