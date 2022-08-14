from fastapi import FastAPI

from . import sample

app = FastAPI()

app.include_router(sample.router)
