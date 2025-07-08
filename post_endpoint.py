from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from helper import 

app=FastAPI()

class User(BaseModel):
    name: str
    age: int

class Message(BaseModel):
    content: str
    user: User

@app.post("/users/", response_model=Message)
def create_user(user: User):
    return {"content": f"User Created Successfully", "user": user}
    