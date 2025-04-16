from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Define Pydantic model
class Item(BaseModel):
    name: str
    description: str
    price: float

# In-memory database
fake_items_db = {}

# Get item by ID
@app.get("/items/{item_id}")
def read_item(item_id: int):
    item = fake_items_db.get(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

# Create new item
@app.post("/items/")
def create_item(item: Item):
    item_id = len(fake_items_db) + 1
    fake_items_db[item_id] = item
    return {"item_id": item_id, "item": item}

# Update existing item
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id not in fake_items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    fake_items_db[item_id] = item
    return {"item_id": item_id, "item": item}

# Delete item
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in fake_items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    del fake_items_db[item_id]
    return {"message": f"Item with id {item_id} deleted successfully"}
