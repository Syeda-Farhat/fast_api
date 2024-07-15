from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
import psycopg2
from psycopg2.extras import RealDictCursor
# import time

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

# below is the db connection and use the while because if the db connection is getting
# failed because of internet issue or any other such tech prob then it keep connecting
# until db connection is estabilshed

# while True:

try:
    conn = psycopg2.connect(
        host="localhost",
        database="fastapi",
        user="postgres",
        password="admin",
        cursor_factory=RealDictCursor,
    )
    cursor = conn.cursor()
    print("successfully connected")
# break
except Exception as error:
    print("connection failed")
    print("Error: ", error)
    # time.sleep(2)

@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/posts")
def get_post():
    cursor.execute("""SELECT * FROM posts """)
    posts = cursor.fetchall()
    return {"data": posts}

# insertion 
@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    cursor.execute(
    """INSERT INTO posts (title, content, published) VALUES (%s, %s, %s)""",
    (post.title, post.content, post.published),)
  # such insertion will take care ffrom sql-injection (using %s)
    new_post = cursor.fetchone()
    conn.commit() # whenever insert any data conn.commit is must 
    return {"data": new_post}


# retriving 
@app.get("/posts/{id}")
def get_post(id: int):
    cursor.execute(
    """INSERT * FROM posts WHERE id = %s""", (str(id),))
    test_post = cursor.fetchone()
    return {"data": test_post}
    