from fastapi import FastAPI
from pydantic import BaseModel
from typing import Set


class SaleDiffRequest(BaseModel):
    old_sale: Set[str]
    new_sale: Set[str]


def sale_diff(
    old_sale: Set[str],
    new_sale: Set[str]
) -> dict:

    # TODO:
    # removed = có trong old_sale nhưng không có trong new_sale
    # added = có trong new_sale nhưng không có trong old_sale
    # kept = có trong cả hai

    pass


app = FastAPI(title="Bai 48")


@app.post("/flash-sale/diff")
def sale_diff_api(request: SaleDiffRequest):
    result = sale_diff(
        request.old_sale,
        request.new_sale
    )

    return result


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)