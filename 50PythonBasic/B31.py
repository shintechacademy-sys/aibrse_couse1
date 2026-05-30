from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional


class Customer(BaseModel):
    name: str
    phone: str


class FindCustomerRequest(BaseModel):
    customers: List[Customer]
    phone: str


def find_customer(
    customers: List[Customer],
    phone: str
) -> Optional[Customer]:

    for customer in customers:
        # TODO
        pass

    return None


app = FastAPI(title="Bai 31")


@app.post("/customers/find-by-phone")
def find_customer_api(request: FindCustomerRequest):
    result = find_customer(
        request.customers,
        request.phone
    )

    return {
        "data": result
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)