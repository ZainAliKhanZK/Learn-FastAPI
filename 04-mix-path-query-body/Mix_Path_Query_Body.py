'''
Path Query Body Combo

- Mix all inputs
- Real - world API structure

'''


from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

users = []

class User(BaseModel):
    name : str
    age : int

@app.post("/users")
def create_user(user : User):
    users.append(user)
    return {"Message" : "User Created!",
            "Data" : user}

@app.put("/users/{user_id}")
def update_user(user_id : int , updated_user : User , notify : bool = False):
    if user_id < len(users):
        users[user_id] = updated_user
        return {"Message" : "User Updated!",
                "Data" : updated_user,
                "notify" : notify}
    return {"Message" : "User Not Found!"}