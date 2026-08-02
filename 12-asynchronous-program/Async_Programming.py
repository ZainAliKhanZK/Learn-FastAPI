'''
ASYNC PROGRAMMING

- async/await
- Why async matters
- Perfomance benefits

'''
from fastapi import FastAPI
import time 
import asyncio

# def task():
#     print("Hello , 1 - 2 - 3")
#     time.sleep(3)
#     print("Hello , 1 - 2 - 3")
#     return "Done"

# print(task())


# async def task():
#     print("Hello , 1 - 2 - 3")
#     await asyncio.sleep(3)
#     print("Hello , 1 - 2 - 3")
#     return "Done"

# res = asyncio.run(task())

# print(res)

app = FastAPI()

@app.get("/")
async def home():
    await asyncio.sleep(3)
    return {
        "Message" : "Async API"
    }