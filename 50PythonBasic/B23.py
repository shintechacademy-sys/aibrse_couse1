from pydantic import BaseModel
from typing import List


class CartItem(BaseModel):
    name: str
    quantity: int


def cart_quantity(cart: List[CartItem]) -> int:
    """
    TODO:
    Tính tổng quantity của tất cả item trong giỏ hàng.
    """

    total_quantity = 0

    for item in cart:
        # TODO
        pass

    return total_quantity