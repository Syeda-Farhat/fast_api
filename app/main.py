from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
import psycopg2
from psycopg2.extras import RealDictCursor
import time

# importing realdictcursor because when we connect db here psycopy2
# does not give the column names it returns only values which is bit confusing 
# without the column names, therefore import realdictcursor display the column 
# name as well, and it is pasing as a parameter in db conn below 

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

while True: 
    try:
        conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='admin', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("successfully connected")
        break
    except Exception as error:
        print("connection failed")
        print("Error: ", error)
        time.sleep(2)

my_posts = [
    {"title": "fastAPI", "content": "working", "id": 1},
    {"title": "FOOD", "content": "Italian", "id": 2},
]










