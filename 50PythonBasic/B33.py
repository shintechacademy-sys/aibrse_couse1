from pydantic import BaseModel
from typing import List


class Order(BaseModel):
    id: int
    is_paid: bool


def paid_orders(orders: List[Order]) -> List[Order]:
    """
    TODO:
    Lọc các đơn hàng có is_paid == True.
    """

    result = []

    for order in orders:
        # TODO
        pass

    return result