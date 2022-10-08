from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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
    return 1

@app.get("api/todo")
async def get_todo():
    """Get all todo items"""
    return 1

@app.get("api/todo{id}")
async def get_todo_by_id(id):
    """Get a todo item by id"""
    return 1

@app.post("api/todo/new")
async def post_todo(data):
    """Create a new todo item"""
    return 1

@app.put("api/todo/edit{id}")
async def edit_todo(id, data):
    """Edit (update) a todo item"""
    return 1

@app.delete("api/todo/delete{id}")
async def delete_todo(id):
    """Edit (update) a todo item"""
    return 1

