from sqlalchemy.orm import sessionmaker
from sqlalchemy import or_
from models import User, engine

Session = sessionmaker(bind=engine)
session = Session()

# we can use the filter method of the query object

# query all users 

users_all = session.query(User).all()

# query all users with age greater than or equal to 30

users_filtered = session.query(User).filter(User.age >= 30).all()
users_filtered = session.query(User).filter(User.age >= 30, User.name=="Lisa").all()

# above statement find all where age is greater than 30 and name must be lisa
print("All Users:", len(users_all))
print("Filtered Users:", len(users_filtered))


# another method to filter

users = session.query(User).filter_by(age=30).all() # in this method we cannot use any condition liek age >= 30 this will give an error 

for user in users:
    print(f"User age: {user.age}")


# another method 

users = session.query(User).where(User.age >= 30).all()

for user in users:
     print(f"User age: {user.age}")

# we can use |(OR) instead of or_ as well but have to form age and name in separate () and also can use AND (&)
# similarly we can use not_, and_

users = session.query(User).where(or_(User.age >= 30, User.name == "Lisa")).all()

for user in users:
     print(f"User age: {user.age} - {user.name}")