from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional


class Product(BaseModel):
    name: str
    price: float


def cheapest_product(products: List[Product]) -> Optional[Product]:
    """
    TODO:
    Tìm sản phẩm có price nhỏ nhất.
    Nếu danh sách rỗng thì return None.
    """
    pass


app = FastAPI(title="Bai 22")


@app.post("/products/cheapest")
def cheapest_product_api(products: List[Product]):
    result = cheapest_product(products)

    return {
        "data": result
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)