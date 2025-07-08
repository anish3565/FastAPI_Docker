from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from helper import demo_save_in_db

app=FastAPI()

class User(BaseModel):
    name: str
    age: int

class Message(BaseModel):
    content: str
    user: User

@app.get("/home")
def get_data():
    return {"message": "hello"}

@app.post("/users/", response_model=Message)
def create_user(user: User):
    return {"content": f"User Created Successfully", "user": user}
    
@app.post("/save/", response_model=str)
def save_data(data: User):
    try:
        result=demo_save_in_db(data)
        return result["status"]
    except Exception as e:
        return HTTPException(status_code=500, detail="Error saving data: {e}")