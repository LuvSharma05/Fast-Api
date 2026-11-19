from fastapi import FastAPI

app=FastAPI()

# @app.get("/users/{user_id}")
# def get_users(user_id):
#     return {"user_id":user_id}


# with datatype(for ex if we give abc in id then it will throw error)
@app.get("/users/{user_id}")
def get_users(user_id:int):
    return {"user_id":user_id}
