from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

todos=[]

class Todo(BaseModel):
    id:int
    title:str
    completed:bool

#Add route
@app.post("/todos")
def create_todo(todo:Todo):
    todos.append(todo)
    return {
        "message":"Todo Added",
        "data":todo
    }


#To get all todos
@app.get("/todos")
def get_todos():
    return todos


#To get a todo
@app.get("/todos/{todo_id}")
def get_todos(todo_id:int):
    for todo in todos:
        if todo.id==todo_id:
            return todo

    return {"error":"Todo not found"}


#To update a todo
@app.put("/todo/{todo_id}")
def update_todo(todo_id:int,updated_todo:Todo):
    for index,todo in enumerate(todos):
        if(todo.id==todo_id):
            todos[index]=updated_todo
            return {"message":"Todo updated","data":updated_todo}

    return {"error":"Todo not found"}


#To delete a todo
#To update a todo
@app.delete("/todo/{todo_id}")
def delete_todo(todo_id:int):
    for index,todo in enumerate(todos):
        if(todo.id==todo_id):
            todos.pop(index)
            return {"message":"Todo deleted","data":todos}

    return {"error":"Todo not found"}

