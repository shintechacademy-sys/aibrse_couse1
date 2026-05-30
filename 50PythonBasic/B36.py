from pydantic import BaseModel
from typing import List, Set


class Product(BaseModel):
    name: str
    category: str


def unique_categories(
    products: List[Product]
) -> Set[str]:
    """
    TODO:
    Trả về set các category không trùng lặp.
    """

    categories = set()

    for product in products:
        # TODO
        pass

    return categories