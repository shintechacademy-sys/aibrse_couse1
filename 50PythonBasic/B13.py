from fastapi import FastAPI
from pydantic import BaseModel


class CustomerRequest(BaseModel):
    total_spent: int


def classify_customer(total_spent: int) -> str:
    """
    TODO:

    normal
    silver
    gold
    """
    pass


app = FastAPI(title="Bai 13")


@app.post("/customers/classify")
def classify_customer_api(request: CustomerRequest):

    result = classify_customer(
        request.total_spent
    )

    return {
        "customer_type": result
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)