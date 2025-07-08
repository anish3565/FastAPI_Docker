from fastapi import FastAPI, HTTPException

app=FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application"}

@app.get("/home")
def read_home():
    return {"home_message": "Hello, World!"}