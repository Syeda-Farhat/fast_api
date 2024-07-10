from sqlalchemy.orm import sessionmaker

from models import User, engine

# inserting entries into the db 

Session = sessionmaker(bind=engine)

session = Session()

user = User(name="John", age=30)
user_2 = User(name="Lisa", age=33)
user_3 = User(name="Harry", age=35)
user_4 = User(name="Rose", age=33)

session.add(user)
session.add_all([user_2, user_3, user_4])

session.commit()

# accessing entries from the database 

users = session.query(User).all()

user = users[0]

print(users)
print(users[2])
print(user)

print(user.id)
print(user.name)
print(user.age)

for user in users:
    print(f"User ID: {user.id}, Name: {user.name}, Age: {user.age}")

user = session.query(User).filter_by(id=1).one_or_none()
user = session.query(User).filter_by(id=1).all()
user = session.query(User).filter_by(id=1).first()

print(users)


# updating the entry 

user = session.query(User).filter_by(id=1).one_or_none()

print(user.name)

user.name = "change name"
print(user.name)

session.delete(user) # deleting the record 

session.commit() # we need to commit the changes then we able to see the change in db

