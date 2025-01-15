from fastapi import FastAPI
from model import User,UserTable
from typing import List
from starlette.middleware.cors import CORSMiddleware

from db import session

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for testing; restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/users")
async def read_users():
    users = session.query(UserTable).all()

    return users


@app.get("/users/{user_id}")
async def read_user(user_id: int):
    user = session.query(UserTable).filter(UserTable.id == user_id).first()

    return user


@app.post("/users")
async def create_user(name : str, age : int):
    user = UserTable()
    user.name = name
    user.age = age
    
    session.add(user)
    session.commit()

    return f"User {name} created successfully"


#user 여러명 업데이트
@app.put("/users")
async def update_user(users: List[User]):
    for user in users:
        user = session.query(UserTable).filter(UserTable.id == user.id).first()
        user.name = user.name
        user.age = user.age
        session.commit()

    return f"Users updated successfully"


'''
#user 한명 업데이트
@app.put("/users/{user_id}")
async def update_user(user_id: int, name : str, age : int):
    user = Session.query(UserTable).filter(UserTable.id == user_id).first()
    user.name = name
    user.age = age
    Session.commit()
    return f"User {name} updated successfully"
'''


@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    user = session.query(UserTable).filter(UserTable.id == user_id).delete()
    session.commit()

    return f"User {user_id} deleted successfully"
