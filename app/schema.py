from pydantic import BaseModel
import Optional
from .import models

class Post (BaseModel):
    title: str
    content: str
    published: bool = True  
    rating: Optional[int] = None