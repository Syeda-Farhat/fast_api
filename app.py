from fastapi import FastAPI
from fastapi.params import Body 
from pydantic import BaseModel
from typing import Optional

app = FastAPI() 

class Post(BaseModel):
    title: str
    content: str
    published: bool = True 
    rating: Optional[int] =  None

my_posts = [{"title": "fastAPI", "content": "working", "id": 1}, {"title": "FOOD", "content": "Italian", "id": 2}]

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p

@app.get("/posts")
def get_post():
    return {"data": my_posts}

@app.get("/posts/{id}")
def get_posts(id):
    print(id)
    post = find_post(int(id))  # having something in path parameter it will always be return an str so we need to conevrt it accordingly, 
    # like here we need id which is int, testing using postman 
    print(post)
    return {"post_detail": post}


# @app.get("/posts/{id}")
# def get_posts(id: int):
#     print(id)
#     post = find_post(id) 
#     print(post)
#     return {"post_detail": post}

