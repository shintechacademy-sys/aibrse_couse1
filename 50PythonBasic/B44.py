from fastapi import FastAPI
from pydantic import BaseModel
from typing import List


class Product(BaseModel):
    id: int
    name: str
    category: str
    rating: float


class RelatedProductRequest(BaseModel):
    product_id: int
    products: List[Product]
    limit: int


def related_products(
    product_id: int,
    products: List[Product],
    limit: int
) -> List[Product]:

    result = []

    # TODO:
    # 1. Tìm category của product_id
    # 2. Lọc sản phẩm cùng category
    # 3. Loại bỏ sản phẩm hiện tại
    # 4. Sắp xếp rating giảm dần
    # 5. Lấy tối đa limit sản phẩm

    return result


app = FastAPI(title="Bai 44")


@app.post("/products/related")
def related_products_api(request: RelatedProductRequest):
    result = related_products(
        request.product_id,
        request.products,
        request.limit
    )

    return {
        "data": result
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)