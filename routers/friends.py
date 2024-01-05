from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from jinja2 import Template

from pydantic import BaseModel

friends = APIRouter(prefix='/friends')
templates = Jinja2Templates(directory="templates")

friends_list = {
    "John": {
        "age": "15",
        "gender": "female",
    },
    "Alice": {
        "age": "20",
        "gender": "female",
    },
    "Bob": {
        "age": "25",
        "gender": "male",
    },
    "Eva": {
        "age": "18",
        "gender": "female",
    }
}


class UserIn(BaseModel):
    username: str


@friends.get('/')
async def friend_get(request: Request):
    return templates.TemplateResponse("friends.html", {"request": request, "friends_list": friends_list})


@friends.post('/')
async def friend_update(user: UserIn):
    name = user.username
    exist = name in friends_list
    if exist:
        return friends_list[name]
    else:
        return {"message": "친구를 찾을 수 없습니다"}


@friends.delete("/{user_id}")
async def friend_delete(user_id: str):
    print(friends_list)
    exist = user_id in friends_list
    if exist:
        del friends_list[user_id]
        return
    else:
        return {"message": "친구를 찾을 수 없습니다"}
