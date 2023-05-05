# William Jonathan Mulyadi
# 2502045683
# L4AC
# * I BASED IT FROM THE IN-CLASS EXAMPLE (STUDENT; FASTAPI)

from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

todos = {
    1: {
        "title": "Math",
        "Description": "Exercise 5",
        "Completed": "True"
    },
    2: {
        "title": "Physics",
        "Description": "Exercise 6",
        "Completed": "False"
    }
}


class Todo(BaseModel):
    title: str
    Description: str
    Status: bool


class Update(BaseModel):
    title: Optional[str] = None
    Description: Optional[str] = None
    Status: Optional[bool] = None

# Endpoints

# POST
# /
# /get-todo/id
# /get-todo_by_title/id

# CREATE
# /create-todo/id

# UPDATE
# /update-todo/id

# DELETE
# /delete-todo/id


# get -----------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
@app.get("/")
def index():
    return {"First data": "Hello World"}


@app.get("/get-todo/{id}")
def get_todo(id: int = Path(description="ID of todo that you want to view")):
    return todos[id]


@app.get("/get-todo_by_title/{id}")
def get_todo_by_title(title: str):
    for id in todos:
        if todos[id]["title"] == title:
            return todos[id]
    return {"Error": "Todo's title is not found"}

# --------------------------------------------------------------------------------------------------------------------
# POST --------------------------------------------------------------------------------------------------------------------


@app.post("/create-todo/{id}")
def add_todo(id: int, todo: Todo):
    if id in todos:
        return {"Error": "Todo ID exists"}
    todos[id] = todo
    return todos[todo]


# --------------------------------------------------------------------------------------------------------------------
# PUT --------------------------------------------------------------------------------------------------------------------


@app.put("/update-todo/{id}")
def update_todo(id: int, todo: Update):
    if id not in todos:
        return {"Error": "Todo ID doesn't exist"}
    if todo[id].title != None:
        todo[id].title = todo.title
    if todo[id].description != None:
        todo[id].description = todo.description
    if todo[id].status != None:
        todo[id].status = todo.status

    return todos[id]

# --------------------------------------------------------------------------------------------------------------------
# DELETE --------------------------------------------------------------------------------------------------------------------


@app.delete("/delete-todo/{id}")
def delete_student(id: int):
    if id not in todos:
        return {"Error": "Todo ID doesn't exist"}
    del todos[id]
    return {"data": "Todo has been deleted successfully"}
