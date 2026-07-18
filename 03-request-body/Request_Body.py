'''
Request Body:

- JSON input handling
- POST request
- Intro To Pydantic
- 

'''

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# @app.post("/create_user")
# def create_user(name: str , age: int):
#     return {"Name" : name ,
#             "age" : age}

class User(BaseModel):
    name : str
    age : int

@app.post("/create_user")
def create_user(user: User):
    return {"Message" : "User Created",
            "data" : user}