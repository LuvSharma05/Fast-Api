from fastapi import FastAPI

app=FastAPI

#home route
@app.get("/")
def home():
    return {"Message":"This is home page"}

#about route
@app.get("/about")
def about():
    return {"Message":"This is about page"}

#users route
@app.get("/users")
def users():
    return {"Message":"This is users page"}
