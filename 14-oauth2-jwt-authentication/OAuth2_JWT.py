'''
OAuth2 + JWT

- Secure Routes
- Token Validation
- Password Hashing

'''

'''
Authentication Basics

- JWT intro (Json Wrapped Token)
- Token-Based auth
- Login API

- Jose : Javascript Object Signature & Encryption (J O S E)

'''

from fastapi import FastAPI, HTTPException, Depends
from jose import jwt, JWTError
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import datetime, timedelta, timezone
from passlib.context import CryptContext 
import bcrypt 

app = FastAPI()

#JWT CONFIG
SECRET_KEY = "mysecret"

ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTE = 30

#PASSWORD HASING SETUP
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated = "auto")

#OAuth SETUP
oauth2_schema = OAuth2PasswordBearer(tokenUrl="login")


# HASH Password
def hash_password(password: str):
    pwd_bytes = password.encode("utf-8")
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(pwd_bytes, salt).decode("utf-8")

# VERIFY Password
def verify_password(plain_password, hashed_password):
    return bcrypt.checkpw(
        plain_password.encode("utf-8"),
        hashed_password.encode("utf-8")
    )

# DUMMY USER DB

fake_user_db = {
    "admin": {
        "username": "admin",
        "hashed_password": hash_password("1234")
    }
}

#CREATE TOKEN
def create_token(data: dict):
    to_encode = data.copy()
    expiry = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTE)

    to_encode.update({
        "exp" : expiry
    })

    token = jwt.encode(to_encode, SECRET_KEY, algorithm= ALGORITHM)

    return token 


#LOGIN API (TOKEN OAuth2 Form)
@app.post("/login")
def login(form_data : OAuth2PasswordRequestForm = Depends()):
    user = fake_user_db.get(form_data.username)
    if not user or not verify_password(form_data.password, user["hashed_password"]):
        raise HTTPException(
            status_code=400,
            detail="Invalid Username of Password"
        )
    access_token = create_token({"sub" : form_data.username})

    return {
        "access_token" : access_token,
        "token_type" : "bearer"
    }

#TOKEN VERIFY
def verify_token(token:str = Depends(oauth2_schema)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")

        if username is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid Token"
            )
        return username
    
    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Invalid Token"
        )

# Protected Route
@app.get("/secure")
def protected_route(username: str = Depends(verify_token)):
    return {
        "Message" : f"Hello {username}, you have access to this route",
        "User" : username
    }