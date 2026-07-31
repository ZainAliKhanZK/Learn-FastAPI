''''
Middleware

- What is Middleware
- Logging middleware
- Request / response flow
'''

from fastapi import FastAPI, Depends , Header, HTTPException, Request
from fastapi.responses import JSONResponse
import time


app = FastAPI()

# @app.middleware("http")
# async def my_middleware(request : Request, call_next):
#     print("Request Recieved")

#     response = await call_next(request)

#     print ("Response Sent")

#     return response

@app.middleware("http")
async def log_middleware(request : Request, call_next):
    start_time = time.time()

    response = await call_next(request)

    process_time = time.time()-start_time

    print(f"Path : {request.url.path} | Time: {process_time}" )

    return response