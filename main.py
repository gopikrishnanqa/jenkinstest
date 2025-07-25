# main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello FastAPI CI!"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id, "message": "This is an item"}

@app.get("/items/{item_id}")
async def reads_itemd(item_id: int):
    return {"item_id": item_id, "message": "This is an item"}
