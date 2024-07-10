from pydantic import BaseModel
from pydantic import ValidationError
# from typing import Optional
# import string

# print(pydantic.__version__) # checking the version of pydantic 

class Person(BaseModel):
    first_name: str 
    last_name: str
    age: int


p = Person(first_name="John", last_name="Smith", age=42)
# print(p)

'''
try:
    Person(first_name="john", last_name="Smith", age="junk")

except ValidationError as ex:
    print(ex)  
'''
# above will show an error because we set int to str the age 

# try:
#     Person(first_name="john", last_name="Smith", age=42)

# except ValidationError as ex:
#     print(ex)  

# print(p.first_name)
# print(p.first_name=="James")
# print(p.age=="qwer")

try:
    Person(first_name="john", last_name="Smith", age="asdf")

except ValidationError as ex:
    exceptions = ex

exceptions.errors() 