from pydantic import BaseModel
from typing import List, Optional


class Product(BaseModel):
    id: str
    name: str


def find_product(
    products: List[Product],
    product_id: str
) -> Optional[Product]:

    for product in products:
        # TODO
        pass

    return None