from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

# @app.post("/create_user")
# def create_user(name:str,age:int):
#     return {
#         "Name":name,
#         "Age":age
#     }

# @app.post("/create_user")
# def create_user(user:dict):
#     return {
#         "message":"User created successfully",
#         "data":user
#     }

class User(BaseModel):
    name:str
    age:int

@app.post("/create_user")
def create_user(user:User):
    return {
        "message":"User created successfully",
        "data":user
    }