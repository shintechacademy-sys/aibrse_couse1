from fastapi import FastAPI
from pydantic import BaseModel
from typing import List


class Product(BaseModel):
    name: str
    category: str


class FilterCategoryRequest(BaseModel):
    products: List[Product]
    category: str


def filter_by_category(
    products: List[Product],
    category: str
) -> List[Product]:
    result = []

    for product in products:
        # TODO
        pass

    return result


app = FastAPI(title="Bai 25")


@app.post("/products/filter-by-category")
def filter_by_category_api(request: FilterCategoryRequest):
    result = filter_by_category(
        request.products,
        request.category
    )

    return {
        "data": result
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)