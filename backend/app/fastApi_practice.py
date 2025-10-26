from typing import Union # Union is type hint from Python's typing module
from fastapi import FastAPI
from pydantic import BaseModel # pydantic enables use of python type hint for data validation

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

@app.get('/')
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
# 'q' can either be a str or None
def read_item(item_id: int, q: Union[str, None] = None): # Union says: If its string then string, if its None then default to 'None'
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}