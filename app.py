from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


my_posts = [
    {"title": "fastAPI", "content": "working", "id": 1},
    {"title": "FOOD", "content": "Italian", "id": 2},
]


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
    post = find_post(
        int(id)
    )  # having something in path parameter it will always be return an str so we need to conevrt it accordingly,
    # like here we need id which is int, testing using postman
    print(post)
    return {"post_detail": post}


# @app.get("/posts/{id}")
# def get_posts(id: int):
#     print(id)
#     post = find_post(id)
#     print(post)
#     return {"post_detail": post}


# in the below route we use response and status
# these are builtin in fastapi we need to import them
# just type status. and it will give all the respose error with bit detail like given below 404
# @app.get("/posts/{id}")
# def get_post(id: int, response: Response):
#     post = find_post(id)
#     if not post:
#         response.status_code = status.HTTP_404_NOT_FOUND
#         return {"message": f"Post with ID: {id} was not found"}
#     return {"post_detail": post}


@app.get("/posts/{id}")
def get_post(id: int, response: Response):
    post = find_post(id)
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with ID: {id} was not found",
        )
    return {"post_detail": post} 


# to change the default status code we have to pass the status code as a path paramter into our route decorator 
# when sending back the error of 204 deleted something, then no back return data

# @app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
# def delete_post(id: int):
#     index = find_index_post(id)
#     my_posts.pop(index)
#     return Response(status_code=status.HTTP_204_NO_CONTENT)

# fastapi automtically generate documentation, go to the url type /docs and gets the complete documentation of all the routes in the fastapi 
# /redoc is also like /docs




