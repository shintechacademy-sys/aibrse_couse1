from pydantic import BaseModel
from typing import List


class User(BaseModel):
    id: int
    username: str
    password: str


def hide_password(
    users: List[User]
):
    """
    TODO:

    Trả về danh sách user
    không chứa password
    """
    pass