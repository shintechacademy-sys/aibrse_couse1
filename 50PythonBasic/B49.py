from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict, Set


class SegmentUserRequest(BaseModel):
    order_counts: Dict[str, int]


def segment_users(
    order_counts: Dict[str, int]
) -> Dict[str, Set[str]]:

    result = {
        "one_time": set(),
        "repeat": set(),
        "vip": set()
    }

    for user_id, count in order_counts.items():
        # TODO:
        # count == 1 => one_time
        # 2 <= count <= 4 => repeat
        # count >= 5 => vip
        pass

    return result


app = FastAPI(title="Bai 49")


@app.post("/customers/segment")
def segment_users_api(request: SegmentUserRequest):
    result = segment_users(request.order_counts)

    return {
        "data": result
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)