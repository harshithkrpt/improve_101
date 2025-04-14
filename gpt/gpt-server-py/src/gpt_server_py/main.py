from typing import Union

from fastapi import FastAPI, Query # type: ignore
from pydantic import BaseModel, AfterValidator # type: ignore

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):        
    return {
        "item_id": item_id,
        "item_name": item.name,
        "price": item.price
    }


# Enum
from enum import Enum
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    other = "other"
    

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if(model_name.value == ModelName.alexnet):
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    if(model_name.value == ModelName.resnet):
        return {"model_name": model_name, "message": "LeCNN all the images"}
    
    return {"model_name": model_name, "message": "Have some residuals"}


# Query Params
@app.get("/query/items/")
async def read_item(skip: int = 0, limit: int | None = None):
    return {
        "skip": skip,
        "limit": limit or 10
    }


# Multi Path and Query Params
@app.get("/multi/query/{item_id}/{user_id}")
async def new_read_item(item_id: str, user_id: int,  query_req: str ,q: Union[str, None] = None, short: bool = False):
    item = {"item_id": item_id, "owner_id": user_id, "queryParamReq": query_req}
    if q:
        item.update({"q": q})
        
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item


class QuerySendingBody(BaseModel):
    name: str
    price: int
    description: str
    float_ptr: float | None = None


# Request Body
@app.post("/send/query")
async def add_data(body: QuerySendingBody):
    return body


# Request Body + Path Params + Query Params
@app.post("/send/query/{item_id}")
async def req_data(body: QuerySendingBody, item_id: int, q: str):
    return {
        "body": body,
        "item_id": item_id,
        "q": q
    }


from typing import Annotated

@app.get("/query/validation")
async def add_query_validation(q: Annotated[str | None, Query(max_length=50, min_length=3, pattern= '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')] = None):
    return {q: q}

@app.get("/query/mul")
async def mul(
    q: Annotated[list[str], Query(title="Testing Title", description="This is a Description",deprecated=True)], 
    item_str: Annotated[str, Query(alias="item-str")],
    hidden_param: Annotated[str | None, Query(include_in_schema=False)] = None):
    return {
        "q": q,
        "item-str": item_str + item_str + "**" + item_str,
        "h": hidden_param
    }


def check(id: str):
    if(id.startswith(("abc", "def"))):
        raise ValueError("SOME ERROR")



@app.get("/query/mmfd")
async def ewew(q: Annotated[str, AfterValidator(check)]):
    return {
        "q": q
    }


def main():
    import uvicorn # type: ignore
    uvicorn.run(app, host="localhost", port=8000)


if __name__ == "__main__":
    main()