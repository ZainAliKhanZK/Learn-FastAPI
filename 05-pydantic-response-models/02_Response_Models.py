'''
Response Models

- Response Validation
- Hide Sensitive Data
- Output Formatting

'''


from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    Name: str
    Age: int
    Password: str

class UserResponse(BaseModel):
    Name: str
    Age: int

@app.get("/user",response_model = UserResponse)
def get_user():
    return {
        "Name" : "Zain",
        "Age" : 21,
        "Password" : 49021
    }