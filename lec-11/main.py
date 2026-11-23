from fastapi import FastAPI,status,HTTPException
from pydantic import BaseModel

app=FastAPI()


#custom exception
class UserNotFoundException(Exception):
    def __int__(self,name:str):
        self.name=name

app.get("/user/{user_name}")
def get_user(name:str):
    if name!="mohit":
        raise UserNotFoundException(name)
    return {
        "name":name
    }