'''
CRUD Operations:

- Create API
- Read API
- Update API
- Delete API
- Example : ToDo API

'''

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

todos = []

class Todo(BaseModel):
    id : int
    title : str
    completed : bool


@app.get("/get_todos") #READ
def get_todos():
    return todos

@app.post("/todos") #CREATE
def create_todo(todo : Todo):
    todos.append(todo)
    return {
            "message" : "Todo Added Successfully",
            "Data" : todo
            }


@app.get("/todos/{todo_id}")
def get_todo(todo_id : int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    return {"Error" : "Todo not Found"}

@app.put("/todos/{todo_id}") #UPDATE
def update_todo(todo_id : int , updated_todo : Todo):
    for index , todo in enumerate(todos):
        if todo.id == todo_id:
            todos[index] = updated_todo
            return {"Message" : "Data Updated",
                    "Data" : updated_todo}


@app.delete("/todos/{todo_id}") #DELETE
def delete_todo(todo_id : int):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos.pop(index)
            return {"Message" :  "Data Deleted"}
    return {"Error" : "Todo Not Found"}

'''
Common HTTP methods used in APIs:

| Method | Purpose              | Example        |
|--------|----------------------|----------------|
|  GET	 | Read/Fetch data      | Get all todos  |
|  POST	 | Create new data      | Add a new todo |
|  PUT	 | Update existing data | Update a todo  |
| DELETE | Remove data          | Delete a todo  |


'''