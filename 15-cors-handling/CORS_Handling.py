"""
CORS Handling

- What is CORS?
- Enable in FastAPI
- Frontend (ReactJS) connection

"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

