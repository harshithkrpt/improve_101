from typing import Union, Literal
from datetime import datetime, time, timedelta

from fastapi import FastAPI, Query, Path, Body, Cookie, Header # type: ignore
from pydantic import BaseModel, AfterValidator, Field, HttpUrl; # type: ignore
from uuid import UUID

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


# Query Parameters with Additional MetaData
@app.get("/app/additional_query")
# Query options -> max_length, min_length, alias, description, title, AfterValidator, deprecated, pattern
async def add_query_param(q: Annotated[str, Query(max_length=20,min_length=4, title="THIS IS A TITLE FOR ADD QUERY PARAM", description="This is a description field", deprecated=True)]):
    return {
        "query": q,
    }


# Path Parameters with Additional Metadata
@app.get("/path/{item_id}")
# ge -> grater equal
# le -> less than equal
# gt -> greater than
# lt -> less then
async def path_param_add_metadata(q: Annotated[int, Path(title="This is a Path Parameter of the Object Id", description="This is the description of the field", ge=1, le=10 )]):
    return {
        "query": q,
    }


# Pydantic Models With Additional Parameters
class FilterParams(BaseModel):
    limit: int = Field(100, gt=0, le=100)
    offset: int = Field(0, ge=0)
    order_by: Literal["created_at", "updated_at"] = "created_at"
    tags: list[str] = []

@app.get("/pydantic_query_param_models")
def pydantic_query_param(query: Annotated[FilterParams, Query()]):
    query_dict = dict(query)
    print(query_dict)
    return {
        "query": query
    }


# Mix Path, Query And Body Parameters
class BodyObject(BaseModel):
    title: str
    description: str
    price: int
    c_gst: float

@app.put("/update/{item_id}")
def update_patch(item_id: int, price: float, item: BodyObject | None = None):
    
    dictionary = {
        "item_id": item_id,
        "price": price,

    }

    if item is not None:
        dictionary.update(item)

    return dictionary

# Adding Body Validations

class BodyValidations(BaseModel):
    price: int | None = Field(default=None, ge=100)
    string: str | None = Field(default=None, max_length=100)

@app.put("/adding/body_fields/api/{item_id}")
def adding_body_fields(item_id: int,body_fields: Annotated[BodyValidations, Body(embed=True)]):
    return {
        "body_fields": body_fields
    }


# Nested Models
class ImageModel(BaseModel):
    url: HttpUrl
    name: str

class ItemModel(BaseModel):
    name: str
    description: str
    image: ImageModel
    field: float = Field(example = [35.4])
    images: list[ImageModel]

@app.put("/items/update/{item_id}")
async def app_items_update(item_id: int, body: ItemModel):
    return {
        "item_id": item_id,
        "body": body
    }


# Declaring Sample Data in Pydantic Model 
class SampleData(BaseModel):
    name: str
    price: float
    list: list[str]
    set: frozenset
  

    # model_config = {
    #     "json_schema_extra": {
    #         "examples": [
    #             {
    #                 "name": "Foo",
    #                 "price": 2.4,
    #                 "list": [
    #                     "one",
    #                     "two"
    #                 ]
    #             }
    #         ]
    #     }
    # }


@app.put("/testing/sample/data")
async def testing_sample_data(body: SampleData):
    return {
        "body": body
    }

@app.put("/extradatatypes/{item_id}")
async def read_items(
    item_id: UUID,
    start_datetime: Annotated[datetime, Body()],
    end_datetime: Annotated[datetime, Body()],
    process_after: Annotated[timedelta, Body()],
    repeat_at: Annotated[time | None, Body()] = None,
):
    start_process = start_datetime + process_after
    duration = end_datetime - start_process
    return {
        "item_id": item_id,
        "start_datetime": start_datetime,
        "end_datetime": end_datetime,
        "process_after": process_after,
        "repeat_at": repeat_at,
        "start_process": start_process,
        "duration": duration,
    }


@app.get("/declare_cookie")
async def declare_cookie(async_id: Annotated[str | None, Cookie()] = None):
    return {
        "id": async_id
    }



class Cookies(BaseModel):
    model_config = {"extra": "forbid"}

    session_id: str
    fatebook_tracker: str | None = None
    googall_tracker: str | None = None

class CommonHeaders(BaseModel):
    host: str
    save_data: bool
    if_modified_since: str | None = None
    traceparent: str | None = None
    x_tag: list[str] = []

@app.get("/get_header")
async def get_header(user_agent: Annotated[str | None , Header()] = None, cookies: Annotated[Cookies | None, Cookie()] = None, headers: Annotated[CommonHeaders | None, Header()] = None):
    return { "User-Agent": user_agent , "cookies":cookies }


# Response Modal -> Return Type
class SameReturnType(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []


@app.post("/same_payload_as_response")
async def same_payload_as_response(spar: SameReturnType) -> SameReturnType:
    return spar

def main():
    import uvicorn # type: ignore
    uvicorn.run(app, host="localhost", port=8000)


if __name__ == "__main__":
    main()