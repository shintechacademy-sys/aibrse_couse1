from pydantic import BaseModel
from typing import List


class Room(BaseModel):
    room: str
    status: str


def available_rooms(
    rooms: List[Room]
) -> int:
    """
    TODO:
    Đếm số phòng có status là "empty".
    """

    count = 0

    for room in rooms:
        # TODO
        pass

    return count