from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict


class Transaction(BaseModel):
    date: str
    amount: float


def daily_report(
    transactions: List[Transaction]
) -> Dict[str, dict]:

    report = {}

    for transaction in transactions:
        # TODO:
        # Gom nhóm theo date
        # Tính total, count, avg
        pass

    return report


app = FastAPI(title="Bai 43")


@app.post("/reports/daily")
def daily_report_api(transactions: List[Transaction]):
    result = daily_report(transactions)

    return {
        "data": result
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)