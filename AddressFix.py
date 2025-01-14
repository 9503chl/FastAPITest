from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional,List
from uuid import UUID,uuid4
from fastapi.middleware.cors import CORSMiddleware

import socket
import ssl

class Item(BaseModel):
    id : Optional[UUID] = uuid4()
    name : str
    price: float
    is_offer: Optional[bool] = None

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for testing; restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

items = []

@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    items.append(item)
    return item

@app.get("/items/", response_model=List[Item])
async def read_items():
    return items

@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: UUID):
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: UUID, item: Item):
    for index, existing_item in enumerate(items):
        if existing_item.id == item_id:
            items[index] = item
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}", response_model=Item)
async def delete_item(item_id: UUID):
    for index, item in enumerate(items):
        if item.id == item_id:
            return items.pop(index)
    raise HTTPException(status_code=404, detail="Item not found")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app, 
        host= "192.168.2.196", 
        port= 8080,
        ssl_keyfile=None,
        ssl_certfile=None
    )