'''
TASK: Understand the following code and run it with swagger docs
TODO: run the code and hit this url
http://127.0.0.1:8000/docs#/
'''

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# In memory database
items_db = []

# Pydantic model for request/response validation
class Item(BaseModel):
    id: int
    name: str
    description: str

@app.post("/items")
def create_item(item: Item):
    if any(existing_item['id'] == item.id for existing_item in items_db):
        return {"Aww, item already exists"}
    items_db.append(item.dict())
    return item

@app.get("/items", response_model=List[Item])
def get_items():
    return items_db

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    for item in items_db:
        if item['id'] == item_id:
            return item
    return {"Item not found"}

@app.put("/items/{item_id}")
def update_item(item_id: int, updated_item: Item):
    for index, item in enumerate(items_db):
        if item['id'] == item_id:
            items_db[index] = updated_item.dict()
            return updated_item
    return {"Item not found"}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for index, item in enumerate(items_db):
        if item['id'] == item_id:
            items_db.pop(index)
            return
    return {"Item not found"}
