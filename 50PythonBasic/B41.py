from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict


class Product(BaseModel):
    id: str
    name: str
    price: float


def build_catalog(
    products: List[Product]
) -> Dict[str, Product]:
    catalog = {}

    for product in products:
        # TODO:
        # Gán product vào catalog theo key là product.id
        pass

    return catalog


app = FastAPI(title="Bai 41")


@app.post("/catalog/build")
def build_catalog_api(products: List[Product]):
    result = build_catalog(products)

    return {
        "data": result
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)