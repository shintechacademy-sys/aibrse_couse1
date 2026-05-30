from fastapi import FastAPI
from pydantic import BaseModel
from typing import List


class Order(BaseModel):
    id: int
    total: float


class AnomalyRequest(BaseModel):
    orders: List[Order]
    threshold: float


def detect_anomalies(
    orders: List[Order],
    threshold: float
) -> List[Order]:

    result = []

    # TODO:
    # Nếu danh sách rỗng return []
    # Tính avg total
    # Lọc order có total > threshold * avg

    return result


app = FastAPI(title="Bai 46")


@app.post("/orders/anomalies")
def detect_anomalies_api(request: AnomalyRequest):
    result = detect_anomalies(
        request.orders,
        request.threshold
    )

    return {
        "data": result
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)