'''
Authentication Basics

- JWT intro (Json Wrapped Token)
- Token-Based auth
- Login API

- Jose : Javascript Object Signature & Encryption (J O S E)

'''

from fastapi import FastAPI, HTTPException, Header, Depends
from jose import jwt
from datetime import datetime, timedelta, timezone

app = FastAPI()

SECRET_KEY = "mysecret"

ALGORITHM = "HS256"

#CREATE TOKEN
def create_token(data: dict):
    to_encode = data.copy()
    expiry = datetime.now(timezone.utc) + timedelta(minutes=30)

    to_encode.update({
        "exp" : expiry
    })

    token = jwt.encode(to_encode, SECRET_KEY, algorithm= ALGORITHM)

    return token 

#LOGIN API (TOKEN GENERATE)
@app.post("/login")
def login(username: str, password: str):
    if username != "admin" or password != "1234":
        raise HTTPException(
            status_code=401,
            detail="Invalid Username and Password"
        )
    token = create_token({
        "sub" : username
    })

    return {
        "access_token" : token
    }

#TOKEN VERIFY
def verify_token(token: str = Header (None)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        return payload
    except:
        raise HTTPException(
            status_code=401,
            detail="Invalid or Expired Token"
        )
    
# PROTECTED ROUTE
@app.get("/secure")
def secure_data(user = Depends(verify_token)):
    return {
        "message" : "Secure Data Accessed",
        "User" : user
    }