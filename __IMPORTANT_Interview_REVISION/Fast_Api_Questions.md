# Questions 

### What is FastAPI and how does it compare to Flask and Django?

- FastAPI is a modern, high-performance web framework for building APIs with Python 3.7+ based on standard type hints. It’s built on Starlette (for web handling) and Pydantic (for data validation). Its key design goal: make API development fast, intuitive, and efficient, while ensuring high performance close to Node.js and Go.

| Feature           | **FastAPI**                       | **Flask**                               | **Django**                                                     |
| ----------------- | --------------------------------- | --------------------------------------- | -------------------------------------------------------------- |
| **Type**          | API-focused, asynchronous         | Lightweight microframework              | Full-stack web framework                                       |
| **Design goal**   | Speed, data validation, async I/O | Simplicity, minimalism                  | Rapid development, batteries-included                          |
| **Async support** | Built-in (async/await native)     | Partial (needs extensions like `Quart`) | Limited (Django 3.1+ supports async views, but not full stack) |


### What are the core design goals and distinguishing features of FastAPI?

- Built on Starlette (for the web layer) and Pydantic (for data validation).
- Uses asynchronous I/O (async / await) to handle thousands of requests concurrently.
- Performance is on par with Node.js and Go, among the fastest Python frameworks.
- Automatic request validation, serialization, and documentation from type hints.
- Less boilerplate → faster development and fewer bugs.
- Fully compliant with OpenAPI (formerly Swagger) and JSON Schema.


### How does FastAPI build on Starlette and Pydantic? Explain responsibilities of each.

- Starlette — the async web foundation
    - ASGI app lifecycle (startup/shutdown events).
    - Routing (path matching, path parameters).
    - HTTP request/response objects and streaming.
    - Middleware support (CORS, sessions, custom middleware).
- Pydantic — the type system & validator
    - Define BaseModel classes that parse and validate incoming data (JSON, query params, headers).
    - Coerce types (e.g., "123" → int), run validators, enforce constraints.
    - Generate JSON-serializable representations (.dict(), .json()).
    - Provide typed models used for request bodies, response models, settings/config.


### Create a minimal FastAPI app with one GET /health endpoint returning {"status":"ok"}.


```py
from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "ok"}

```

- run

```py
uvicorn main:app --reload
```

### Add a GET /hello/{name} endpoint that returns {"message":"Hello, <name>!"}.


```py
from fastapi import FastAPI

app = FastAPI()

@app.get("/hello/{name}")
def get_hello(name: str):
    return {
        "message": f"Hello, {name}!"
    }
```

### Show how to run the app with Uvicorn from Python (programmatically) and explain why Uvicorn is used.

```py
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/hello/{name}")
def get_hello(name: str):
    return {"message": f"Hello, {name}!"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True)

```



### Difference between path, query, and header parameters in FastAPI.

```py
# path params

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}

# query params
@app.get("/users")
def list_users(limit: int = 10, offset: int = 0):
    return {"limit": limit, "offset": offset}
```

- header

```py
from fastapi import Header

@app.get("/data")
def read_data(user_agent: str = Header(...)):
    return {
        "user_agent": user_agent
    }
```

###  5. How does FastAPI do automatic parameter validation and conversion?

```py
@app.get("/items/{item_id}")
def read_item(item_id: int):   # "42" -> 42 (int), invalid -> 422
    return {"item_id": item_id}

```

```py
from fastapi import Query

@app.get("/search")
def search(q: str = Query(..., min_length=3, max_length=50), page: int = 1):
    return {"q": q, "page": page}

```

- good example

```py
from typing import List, Optional

from fastapi import FastAPI, Header, Query, Path, HTTPException
from pydantic import BaseModel, Field, validator

app = FastAPI()


class ItemIn(BaseModel):
    name: str = Field(..., min_length=1, max_length=50, description="Item name")
    price: float = Field(..., gt=0, description="Price must be > 0")
    tags: List[str] = Field(default_factory=list)
    discount: Optional[float] = Field(None, ge=0, description="Optional discount amount")

    @validator("name")
    def name_no_digits(cls, v: str) -> str:
        if any(ch.isdigit() for ch in v):
            raise ValueError("name must not contain digits")
        return v

    @validator("discount")
    def discount_less_than_price(cls, v, values):
        price = values.get("price")
        # Only validate if both provided
        if v is not None and price is not None and v >= price:
            raise ValueError("discount must be less than price")
        return v


class ItemOut(BaseModel):
    id: int
    name: str
    price: float
    tags: List[str]
    final_price: float


@app.post(
    "/items/{item_id}",
    response_model=ItemOut,
    summary="Create an item (demo: path+query+header+body validation)",
)
def create_item(
    item_id: int = Path(..., ge=1, description="Numeric ID of the item"),
    q: str = Query(..., min_length=3, description="Search/query string (min 3 chars)"),
    page: int = Query(1, ge=1, description="Page number, >= 1"),
    x_request_id: Optional[str] = Header(None, alias="X-Request-ID"),
    item: ItemIn = ...,
):
    """
    Example endpoint that:
    - validates `item_id` (path)
    - validates `q` and `page` (query)
    - reads `X-Request-ID` (header)
    - validates request body via `ItemIn` (Pydantic, incl. custom validators)
    """
    # Example of reacting to missing header (optional behavior)
    if x_request_id is None:
        # Not required — but we can enforce policy at runtime
        raise HTTPException(status_code=400, detail="X-Request-ID header is recommended")

    # Business logic: compute final price after discount (if any)
    final_price = item.price - (item.discount or 0.0)

    return ItemOut(
        id=item_id,
        name=item.name,
        price=item.price,
        tags=item.tags,
        final_price=final_price,
    )

```

### Explain path operation priority and overlap (e.g., /items/{id} vs /items/new)

FastAPI (built on Starlette) matches routes from top to bottom in the order they are defined in your code.

That means:
First match wins.

- Both match /items/123 and /items/abc — so FastAPI raises an error at startup.
You cannot define two routes with the same pattern structure, even if variable names differ.

```py
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/items/{item_name}")
def read_item_by_name(item_name: str):
    return {"item_name": item_name}

```