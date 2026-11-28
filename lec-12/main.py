from fastapi import FastAPI,Depends,Header,HTTPException

app=FastAPI()


#1
# def common_logic():
#     return {
#         "message":"Common Logic Executed"
#     }

# @app.get("/home")
# def home(data=Depends(common_logic)):
#     return data

#2-> Auth example 
def verify_token(token:str=Header(None)):
    if token!="mysecret":
        raise HTTPException(
            status_code=401,
            detail="Unauthorized"
        )
    return {
        "user": "Authorized User"
    }


@app.get("/secure-data")
def secure_data(user=Depends(verify_token)):
    return {
        "message":"Secure data accessed",
        "user":user
    }