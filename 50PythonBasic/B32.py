from pydantic import BaseModel
from typing import List


class User(BaseModel):
    username: str


def username_exists(
    users: List[User],
    username: str
) -> bool:
    """
    TODO:
    Kiểm tra username đã tồn tại trong danh sách users chưa.
    """

    for user in users:
        # TODO
        pass

    return False