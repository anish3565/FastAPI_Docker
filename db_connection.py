from fastapi import FastAPI
from contextlib import contextmanager
from pydantic import BaseModel

app=FastAPI()

DATABASE_URL = "sqlite:///./test.db"

class SessionLocal:
    def start(self):
        # Simulate starting a session
        print("Session started")
        return self
    
    def close(self):
        # Simulate closing a session
        print("Session closed")


class User(BaseModel):
    name: str
    age: int

@contextmanager
def get_db():
    db=SessionLocal()
    try:
        yield db.start()
    finally:
        db.close()

@app.post("/save/")
def save_data(user: User):
    with get_db() as db:
        # Simulate saving data to the database
        print(f"Saving user: {user}")
        return {"status": "Data saved successfully!"}