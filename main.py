from fastapi import FastAPI

app = FastAPI()

# Home endpoint
@app.get("/")
async def read_root():
    return {"message": "Hello, World!"} 

# Endpoint to get an item by ID
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}