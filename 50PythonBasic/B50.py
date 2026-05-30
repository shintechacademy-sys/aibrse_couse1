from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict, Set, List


class ConflictRequest(BaseModel):
    flash_sale_items: Set[str]
    active_campaigns: Dict[str, Set[str]]


def check_conflicts(
    flash_sale_items: Set[str],
    active_campaigns: Dict[str, Set[str]]
) -> dict:

    conflicts = {}
    safe_items = set()

    for product_id in flash_sale_items:
        # TODO:
        # Kiểm tra product_id có nằm trong campaign nào không
        # Nếu có thì thêm vào conflicts
        # Nếu không thì thêm vào safe_items
        pass

    return {
        "has_conflict": len(conflicts) > 0,
        "conflicts": conflicts,
        "safe_items": safe_items
    }


app = FastAPI(title="Bai 50")


@app.post("/campaigns/check-conflicts")
def check_conflicts_api(request: ConflictRequest):
    result = check_conflicts(
        request.flash_sale_items,
        request.active_campaigns
    )

    return result


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)