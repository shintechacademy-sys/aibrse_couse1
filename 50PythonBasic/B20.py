from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    role: str


def is_admin(user: User) -> bool:
    """
    TODO:

    role == admin
    """
    pass