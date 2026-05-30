from pydantic import BaseModel
from typing import List


class Order(BaseModel):
    id: int
    total: float


def high_value_orders(
    orders: List[Order],
    min_total: float
) -> List[Order]:

    result = []

    for order in orders:
        # TODO
        pass

    return result