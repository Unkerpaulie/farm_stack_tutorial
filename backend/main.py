from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from model import Todo

import database as db

# app object
app = FastAPI()

origins = ["https://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# endpoint methods
@app.get("/")
def read_root():
    return {"msg": "Hello!"}

@app.get("api/todo")
async def get_todo():
    """Get all todo items"""
    response = await db.fetch_all_items()
    return response

@app.get("api/todo{title}", response_model=Todo)
async def get_todo_by_title(title):
    """Get a todo item by title"""
    response = await db.fetch_one_item(title)
    if response:
        return response
    raise HTTPException(404, f"The item: \"{title}\" was not found.")

@app.post("api/todo/new", response_model=Todo)
async def new_todo(data):
    """Create a new todo item"""
    response = await db.create_item(data.dict)
    if response:
        return response
    raise HTTPException(400, f"Something went wrong.")
    
@app.put("api/todo/edit{title}")
async def edit_todo(title, data):
    """Edit (update) a todo item"""
    return 1

@app.put("api/todo/check{title}")
async def check_todo(title):
    """Toggle a todo item's done status"""
    response = await db.check_item(title)
    if response:
        return response
    raise HTTPException(404, f"The item: \"{title}\" was not found.")

@app.delete("api/todo/delete{title}")
async def delete_todo(title):
    """Delete a todo item"""
    response = await db.delete_item(title)
    if response:
        return {"msg": f"Successfully deleted item: \"{title}\""}
    raise HTTPException(404, f"The item: \"{title}\" was not found.")

