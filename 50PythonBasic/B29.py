from pydantic import BaseModel
from typing import List


class Ticket(BaseModel):
    id: int
    priority: str


def count_urgent(tickets: List[Ticket]) -> int:
    """
    TODO:
    Đếm số ticket có priority là "urgent".
    """

    count = 0

    for ticket in tickets:
        # TODO
        pass

    return count