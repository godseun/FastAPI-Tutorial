from enum import Enum

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    """
    test

    ____
    param: aa
    """
    return {"message": "Hello World"}
