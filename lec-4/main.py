from fastapi import FastAPI

app=FastAPI()

# @app.get("/users")
# def get_users(name):
#     return {"Name":name}




#optional parameter

@app.get("/users")
def get_users(name:str=None):
    return {"Name":name}


#default values
@app.get("/product")
def get_users(limit:int=10):
    return {"Limit":limit}

@app.get("/items")
def get_users(name:str="none",price:int=0):
    return {
        "Name":name,
        "Price":price
    }



