from fastapi import FastAPI
from pydantic import BaseModel
from typing import List


class Transaction(BaseModel):
    amount: float
    status: str


def daily_revenue(
    transactions: List[Transaction]
) -> float:

    total = 0

    for transaction in transactions:
        # TODO
        pass

    return total


app = FastAPI(title="Bai 17")


@app.post("/revenue/daily")
def daily_revenue_api(
    transactions: List[Transaction]
):

    total = daily_revenue(transactions)

    return {
        "revenue": total
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)