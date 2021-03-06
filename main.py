from enum import Enum

from fastapi import FastAPI
from fastapi.responses import StreamingResponse

from pydantic import BaseModel, Field, validator

app = FastAPI()

class FooRequest(BaseModel):
    product_id: int = Field(..., example=100323)
    user_id: int = Field(..., example=5532)

    @validator("product_id", "user_id")
    def validate_id(cls, v):
        assert v.digit(), "mustbe digit"



class BarResponse(BaseModel):
    product_name: str = Field(..., example="아이폰")


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


some_file_path = "./video.mp4"

@app.get("/stream")
async def video_streamer():
    file_like = open(some_file_path, mode="rb")
    return StreamingResponse(file_like, media_type="video/mp4")


@app.post("/foo", response_model=BarResponse)
async def foo(Bar: FooRequest) -> dict:
    ...
    return {"product_name": "아이폰"}


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
