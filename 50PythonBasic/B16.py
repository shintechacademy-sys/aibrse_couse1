from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional


class Order(BaseModel):
    id: int


def latest_order(
    orders: List[Order]
) -> Optional[Order]:

    """
    TODO:

    Tìm order có id lớn nhất

    Nếu rỗng:
        return None
    """
    pass


app = FastAPI(title="Bai 16")


@app.post("/orders/latest")
def latest_order_api(
    orders: List[Order]
):

    result = latest_order(orders)

    return {
        "data": result
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)