from fastapi import FastAPI, HTTPException, Path
from pydantic import BaseModel
from typing import Annotated, List


class User(BaseModel):
    id: int
    username: str
    age: int


app = FastAPI()

users: List[User] = []


@app.get("/users", response_model=List[User])
async def get_users():
    return users


@app.post("/user/{username}/{age}", response_model=User)
async def create_user(
        username: Annotated[str, Path(min_length=5, max_length=20, description="Username")],
        age: Annotated[int, Path(ge=18, le=120, description="Age")]
):
    next_id = 1 if not users else users[-1].id + 1
    new_user = User(id=next_id, username=username, age=age)
    users.append(new_user)
    return new_user


@app.put("/user/{user_id}/{username}/{age}", response_model=User)
async def update_user(
        user_id: Annotated[int, Path(ge=1, description="User ID")],
        username: Annotated[str, Path(min_length=5, max_length=20, description="Username")],
        age: Annotated[int, Path(ge=18, le=120, description="Age")]
):
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail="User was not found")


@app.delete("/user/{user_id}", response_model=User)
async def delete_user(user_id: Annotated[int, Path(ge=1, description="User ID")]):
    for i, user in enumerate(users):
        if user.id == user_id:
            deleted_user = users.pop(i)
            return deleted_user
    raise HTTPException(status_code=404, detail="User was not found")
