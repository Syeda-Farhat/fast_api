from pydantic import BaseModel
import Optional
from .import models

# class Post(BaseModel):
#     title: str
#     content: str
#     published: bool = True  
    # rating: Optional[int] = None


# class CreatePost(BaseModel):
#     title: str
#     content: str
#     published: bool = True 

# class UpdatePost(BaseModel):
#     published: bool

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass
