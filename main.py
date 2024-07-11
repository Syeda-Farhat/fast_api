from fastapi import FastAPI
from fastapi.params import Body 
from pydantic import BaseModel
from typing import Optional

app = FastAPI() # this is the fastApi instance 

# model (pydantic)
class Post(BaseModel):  # for testing purpose we can pass these in postman in json body 
    title: str
    content: str
    published: bool = True # setting by default value, like optional 
    rating: Optional[int] =  None


my_posts = [{"title": "fastAPI", "content": "working", "id": 1}, {"title": "FOOD", "content": "Italian", "id": 2}]

# below know as route and path operations (fastapi doc)

@app.get("/")
# async def root(): # async is optional like when we are doing some async task
def root():
    return {"message": "Hello World"}

# fastapi automatically convert to json, json is universal language for apis
# @app.get("/") here get is http method and / is URL path. and with @ its a decorator function

@app.get("/posts")
def get_post():
    return {"data": my_posts}  # line 16 my_posts

# if using same url path then order matters for fastapi, it will excute the first one first 

# @app.post("/createposts")
# def create_post(payload: dict = Body(...)):
#     print(payload)
#     return {"new_post": f"title {payload["title"]} content: {payload["content"]}"}

@app.post("/createposts")
def create_post(new_post: Post):
    print(new_post.title) # this will return only title, like we can take single property of the model as well
    print(new_post) # this will print both title and content which we passed in our basemodel
    print(new_post.published)  # this is an optional field for a schema 
    # print(new_post.dict())    # instead of this we can use the following line given below for the latest version
    print(new_post.model_dump())
    return {"data": "new data"}

# The model_dump() method converts your Pydantic model instance to a dictionary,
# similar to how dict() was used in Pydantic v1.
# This allows you to see the data stored in the Pydantic model in a dictionary format,
# which is often useful for debugging or serialization.

