#Сайланкин Дамир 107b
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import uvicorn

app = FastAPI()

class User(BaseModel):
    index: int
    name: str
    role: str

users = []

@app.get("/")
def read_root():
    return {"message": "Hello world!"}

@app.post("/user")
def create_user(user: User):
    for existing_user in users:
        if existing_user.index == user.index:
            raise HTTPException(status_code=400, detail="User with this index already exists")
    users.append(user)
    return {"message": "User created successfully"}

@app.get("/user", response_model=List[User])
def get_users():
    return users

@app.get("/user/{user_index}", response_model=User)
def get_user(user_index: int):
    for user in users:
        if user.index == user_index:
            return user
    raise HTTPException(status_code=404, detail="User not found")

@app.delete("/user/{user_index}")
def delete_user(user_index: int):
    global users
    user_to_delete = None
    for user in users:
        if user.index == user_index:
            user_to_delete = user
            break

    if user_to_delete:
        users.remove(user_to_delete)  
        return {"message": "User deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="User not found")


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)