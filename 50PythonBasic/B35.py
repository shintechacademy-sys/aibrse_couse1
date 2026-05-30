from fastapi import FastAPI
from pydantic import BaseModel
from typing import Set


class WishlistRequest(BaseModel):
    product_id: str
    wishlist: Set[str]


def is_wishlisted(
    product_id: str,
    wishlist: Set[str]
) -> bool:
    """
    TODO:
    Kiểm tra product_id có nằm trong wishlist không.
    """
    pass


app = FastAPI(title="Bai 35")


@app.post("/wishlist/check")
def is_wishlisted_api(request: WishlistRequest):
    result = is_wishlisted(
        request.product_id,
        request.wishlist
    )

    return {
        "is_wishlisted": result
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)