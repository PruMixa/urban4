from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get("/users")
async def get_users():
    return users


@app.post("/user/{username}/{age}")
async def create_user(
        username: Annotated[str, Path(min_length=5, max_length=20, description="Enter_Username", examples="5")],
        age: Annotated[int, Path(ge=18, le=120, description="Age", examples="24")]
) -> str:
    if users:
        next_user_id = str(max(int(user_id) for user_id in users.keys()) + 1)
    else:
        next_user_id = '1'

    new_user_info = f"Имя: {username}, возраст: {age}"
    users[next_user_id] = new_user_info
    message = f"User {next_user_id} is registered"
    return message


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(
        user_id: Annotated[int, Path(ge=1, description="User ID", examples="1")],
        username: Annotated[str, Path(min_length=5, max_length=20, description="Username", examples="UrbanUser")],
        age: Annotated[int, Path(ge=18, le=120, description="Age", examples="24")]
) -> str:
    if str(user_id) in users:
        users[str(user_id)] = f"Имя: {username}, возраст: {age}"
        return f"The user {user_id} is updated"
    else:
        return {"error": f"User with ID {user_id} not found"}


@app.delete("/user/{user_id}")
async def delete_user(user_id: Annotated[int, Path(ge=1, description="User ID", examples="1")]):
    if str(user_id) in users:
        del users[str(user_id)]
        return f"User {user_id} has been deleted"
    else:
        return {"error": f"User with ID {user_id} not found"}
