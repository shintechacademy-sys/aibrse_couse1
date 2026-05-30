from fastapi import FastAPI
from pydantic import BaseModel


class OrderStatusRequest(BaseModel):
    status: str


def order_message(status: str) -> str:
    """
    TODO:
    pending
    confirmed
    shipping
    completed
    cancelled
    """
    pass


app = FastAPI(title="Bai 04")


@app.post("/orders/message")
def order_message_api(request: OrderStatusRequest):
    message = order_message(request.status)

    return {
        "message": message
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)