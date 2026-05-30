from fastapi import FastAPI
from pydantic import BaseModel
from typing import List


class Product(BaseModel):
    id: int
    name: str
    stock: int
    is_active: bool


def filter_available(products: List[Product]) -> List[Product]:
    result = []

    for product in products:
        # TODO
        pass

    return result


app = FastAPI(title="Bai 01")


@app.post("/products/available")
def filter_available_api(products: List[Product]):
    result = filter_available(products)

    return {
        "data": result
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)