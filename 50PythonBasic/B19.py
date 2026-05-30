from fastapi import FastAPI
from pydantic import BaseModel


class OrderCodeRequest(BaseModel):
    order_id: int


def order_code(order_id: int) -> str:
    """
    TODO:

    ORD-00027
    """
    pass


app = FastAPI(title="Bai 19")


@app.post("/orders/code")
def order_code_api(
    request: OrderCodeRequest
):

    code = order_code(
        request.order_id
    )

    return {
        "order_code": code
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)