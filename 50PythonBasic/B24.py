from fastapi import FastAPI
from pydantic import BaseModel
from typing import List


class CouponRequest(BaseModel):
    code: str
    coupons: List[str]


def coupon_exists(code: str, coupons: List[str]) -> bool:
    """
    TODO:
    Kiểm tra code có nằm trong coupons không.
    """
    pass


app = FastAPI(title="Bai 24")


@app.post("/coupons/check")
def coupon_exists_api(request: CouponRequest):
    result = coupon_exists(request.code, request.coupons)

    return {
        "exists": result
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)