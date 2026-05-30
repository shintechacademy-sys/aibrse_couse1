from fastapi import FastAPI
from pydantic import BaseModel
from typing import List


class CartItem(BaseModel):
    name: str
    price: float
    quantity: int


def cart_total(cart: List[CartItem]) -> float:
    total = 0

    for item in cart:
        # TODO
        pass

    return total


app = FastAPI(title="Bai 02")


@app.post("/cart/total")
def cart_total_api(cart: List[CartItem]):
    total = cart_total(cart)

    return {
        "total": total
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)