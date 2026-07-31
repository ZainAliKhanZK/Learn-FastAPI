'''
Database Intergration
(SQLite)

- What is SQLite
- Setup DB
- Connect FastAPI with DB
- SQLite vs SQLAlchemy

'''


from fastapi import FastAPI
import sqlite3

app = FastAPI()

@app.get("/")
def home():
    return {
        "message" : "SQLite Connected Fine"
    }
    

conn = sqlite3.connect("test.db", check_same_thread= False)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS todos(
               id INT PRIMARY KEY,
               title TEXT,
               completed TEXT
               )
""")

conn.commit()
