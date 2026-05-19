from typing import List

class Product:
    def __init__(self, id: int, name: str, stock: int, is_active: bool):
        self.id = id
        self.name = name
        self.stock = stock
        self.is_active = is_active

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "stock": self.stock,
            "is_active": self.is_active
        }


# 2. hàm lọc sản phẩm còn hàng và đang active

def filter_available(products: List[Product]) -> List[Product]:
    """
    Lọc sản phẩm còn hàng và đang active.

    Input:
        products: List[Product]

    Output:
        List[Product]
    """
    result = []

    for product in products:
        if product.stock > 0 and product.is_active is True:
            result.append(product)

    return result