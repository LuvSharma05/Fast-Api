# from fastapi import FastAPI,status,HTTPException
# from pydantic import BaseModel

# app=FastAPI()


# #custom exception
# class UserNotFoundException(Exception):
#     def __int__(self,name:str):
#         self.name=name

# @app.get("/user/{user_name}")
# def get_user(name:str):
#     if name!="mohit":
#         raise UserNotFoundException(name)
#     return {
#         "name":name
#     }



#Global Exception handler

from fastapi import FastAPI,status,Request
from fastapi.responses import JSONResponse

app=FastAPI()

#custom exception
class UserNotFountException(Exception):
    def __init__(self,name:str):
        self.name=name

@app.exception_handler(UserNotFountException)
def user_not_found_handler(request:Request,exc:UserNotFountException):
    return JSONResponse(
        status_code=404,
        content={
            "status":"error",
            "message":f"User {exc.name} not found"
        }
    )


@app.get("/user/{user_name}")
def get_user(name:str):
    if name!="mohit":
        raise UserNotFountException(name)
    return {
        "name":name
    }