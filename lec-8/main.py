
from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

users=[]

class User(BaseModel):
    name:str
    age:int


@app.post("/users")
def create_user(user:User):
    users.append(user)
    return {
        "message":"User Created",
        "data":user
    }


@app.put("/users/{user_id}")
def update_user(user:User,user_id:int,notify:bool=False):
    if user_id<len(users):
        return {
            "message":"User updated",
            "notify":notify,
            "data":user
        }

    return {"message":"User not found"}