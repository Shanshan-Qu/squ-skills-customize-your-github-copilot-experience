# Building REST APIs with FastAPI
# Assignment: Define routes and handle POST requests with validation
#
# Run this app with:
#   uvicorn starter-code:app --reload
#
# Then visit http://127.0.0.1:8000/docs for the interactive API docs.

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# In-memory storage for items
items = []


# TODO: Task 1 - Define a GET endpoint at "/" that returns a welcome message
@app.get("/")
def read_root():
    pass  # Replace with a return statement


# TODO: Task 1 - Define a GET endpoint at "/items" that returns the full items list
@app.get("/items")
def get_items():
    pass  # Replace with a return statement


# TODO: Task 1 - Define a GET endpoint at "/items/{item_id}" that returns a single item by its index
@app.get("/items/{item_id}")
def get_item(item_id: int):
    pass  # Replace with logic to look up and return the item, or return a 404 if not found


# TODO: Task 2 - Define a Pydantic model called "Item" with fields: name (str), price (float), description (str)
class Item(BaseModel):
    pass  # Add fields here


# TODO: Task 2 - Define a POST endpoint at "/items" that accepts an Item body, appends it to `items`, and returns it
@app.post("/items", status_code=201)
def create_item(item: Item):
    pass  # Add logic to store and return the new item
