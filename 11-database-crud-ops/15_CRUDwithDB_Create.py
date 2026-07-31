"""
CRUD with Database
(CREATE - Insert Data)

- SQLAlchemy 
- What is CREATE?
- Flow of CREATE API
- Testing with Swagger UI & DB

"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from sqlalchemy import Column, Integer, String
from fastapi import FastAPI, Depends

app = FastAPI()

# Database URL 
DATABASE_URL = "sqlite:///./test.db"

# Engine Create( DB connection )
engine = create_engine(
    DATABASE_URL,
    connect_args= {"check_same_thread" : False}
)

# Session Creation (For DB Operations)
sessionLocal = sessionmaker(bind=engine)

# Base (For Model)
Base = declarative_base()

# Table (Model)
class Todo(Base):
    __tablename__ = "Todos"

    id = Column(Integer, primary_key=True , index=True)
    title = Column(String)
    completed = Column(String)

Base.metadata.create_all(bind=engine)

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

# @app.get("/")
# def home(db: Session = Depends(get_db)):
#     return {
#         "message" : "DB connected fine"
#     }

# CREATE API

@app.post("/todos")
def create_todo(title : str, db : Session = Depends(get_db)):
    todo = Todo(title = title, completed = "False")
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return {
        "Message" : "Todo Created",
        "data" : todo
    }