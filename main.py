from enum import Enum

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class FooRequest(BaseModel):
    product_id: int = Field(..., example=100323)
    user_id: int = Field(..., example=5532)


class BarResponse(BaseModel):
    product_name: str = Field(..., example="아이폰")


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.post("foo", response_model=BarResponse)
async def foo(Bar: FooRequest) -> dict:
    ...
    return ...


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName) -> dict:
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}
    
    return {"model_name": model_name, "message": "Have some residuals"}


@app.get("/users/me")
async def read_user_me() -> dict:
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


@app.get("/items/{item_id}")
async def read_item(item_id: int) -> dict:
    return {"item_id": item_id}


@app.get("/")
async def read_main() -> dict:
    """
    test

    ____
    param: aa
    """
    return {"message": "Hello World"}
