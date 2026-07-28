''''
Dependency Injection in FastAPI

- What is Depends()
- Reusable Logics
- Auth Example intro
'''

from fastapi import FastAPI, Depends , Header, HTTPException
from fastapi.responses import JSONResponse

app = FastAPI()


# def common_logic():
#     return {
#         "Message" : "Common Logic Executed"
#     }

# @app.get("/home")
# def home(data = Depends(common_logic)):
#     return data 

# def get_current_user():
#     return {
#         "user" : "Zain"
#     }

# @app.get("/profile")
# def profile(user = Depends(get_current_user)):
#     return user

# @app.get("/dashboard")
# def profile(user = Depends(get_current_user)):
#     return user

def verify_token(token : str = Header(None)):
    if token != "mysecrettoken":
        raise HTTPException(
            status_code=401,
            detail="Unauthorized"
        )
    return {
        "users" : "Authorized User"
    }

@app.get("/secure_data")
def secure_data(user = Depends(verify_token)):
    return {
        "message" : "Secure Data Accessed",
        "user" : user
    }