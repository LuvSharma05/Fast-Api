from fastapi import FastAPI

app=FastAPI()

# @app.get("/users")
# def get_users(name):
#     return {"Name":name}




#optional parameter

@app.get("/users")
def get_users(name:str=None):
    return {"Name":name}



