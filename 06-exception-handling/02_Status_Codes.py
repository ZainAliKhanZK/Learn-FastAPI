'''
Status Codes & Responses
- HTTP status code
- Custom responses 
- Error handling basics

'''

from fastapi import FastAPI , status , HTTPException

app = FastAPI()

@app.post("/create_user",status_code= status.HTTP_201_CREATED)
def create_user():
    return{
        "Message" : "User Created!"
    }

@app.get("/users")
def get_users():
    return{
        "status" : "Success",
        "message" : "User Fetched!",
        "data" : {
            "Name" : "Zain", 
             "Age" : 21
             }
    }

@app.get("/user/{user_id}")
def get_user(user_id: int):
    if user_id != 1:
        raise HTTPException(
            status_code=404,
            detail="User Not Found"
        )
    return {
        "id" : 1,
        "name" : "Zain"
    }
