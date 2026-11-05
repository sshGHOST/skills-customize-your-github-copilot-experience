from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Item API")

# In-memory storage for items
items = [
    {"id": 1, "name": "Laptop", "description": "Portable computer"},
    {"id": 2, "name": "Mouse", "description": "Used for pointing"},
]


class Item(BaseModel):
    id: int
    name: str
    description: str


# TODO: Create a GET / endpoint that returns a welcome message

# TODO: Create a GET /items endpoint that returns all items

# TODO: Create a POST /items endpoint that adds a new item

# TODO: Create a GET /items/{item_id} endpoint that returns one item

# TODO: Handle missing items with HTTPException
