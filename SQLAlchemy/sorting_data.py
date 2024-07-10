import random 
from sqlalchemy.orm import sessionmaker
from models import User, engine

Session = sessionmaker(bind=engine)
session = Session()


# populate the User table with this data 

# names = ["Alice", "Bob", "Charlie", "David", "Eve"]
# age =[27, 29, 30, 31, 28]

# for x in range(6):
#     user = User(name=random.choice(names), age=random.choice(age))
#     session.add(user)

# session.commit()

# query all users ordered by age (ascending)

users = session.query(User).order_by(User.age).all()
# users = session.query(User).order_by(User.age.dec()).all()  # sorting in decending order
#similarly we can sort the data using names as well, by passing argument in order_by
# like order_by(User.age, User.name)


for user in users:
    print(f"User ID: {user.id}, Name: {user.name}, Age: {user.age}")



