from fastapi import FastAPI

app = FastAPI() # this is the fastApi instance 


# below know as route and path operations (fastapi doc)

@app.get("/")
# async def root(): # async is optional like when we are doing some async task
def root():
    return {"message": "Hello World"}

# fastapi automatically convert to json, json is universal language for apis
# @app.get("/") here get is http method and / is URL path. and with @ its a decorator function

@app.get("/posts")
def get_post():
    return {"data": "This is your post"}

# if using same url path then order matters for fastapi, it will excute the first one first 


