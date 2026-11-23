from fastapi import FastAPI,status,HTTPException
from pydantic import BaseModel

app=FastAPI()

#status code
@app.post("/create_user",status_code=status.HTTP_201_CREATED)
def create_user():
    return {
        "message":"User Created"
    }

@app.get("/user")
def get_user():
    return {
        "status":"Success",
        "message":"User Fetched",
        "data":{
            "name":"Mohit"
        }
    }

@app.get("/users/{user_id}")
def get_users(user_id:int):
    if user_id!=1:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    return {
        "id":1,
        "name":"Mohit"
    }