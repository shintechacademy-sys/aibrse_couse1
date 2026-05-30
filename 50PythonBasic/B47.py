from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict, List


class RbacRequest(BaseModel):
    role: str
    resource: str
    action: str
    rbac: Dict[str, Dict[str, List[str]]]


def can_access(
    role: str,
    resource: str,
    action: str,
    rbac: Dict[str, Dict[str, List[str]]]
) -> bool:

    # TODO:
    # Kiểm tra role có tồn tại không
    # Kiểm tra resource có tồn tại trong role không
    # Kiểm tra action có nằm trong danh sách quyền không

    pass


app = FastAPI(title="Bai 47")


@app.post("/rbac/check")
def can_access_api(request: RbacRequest):
    result = can_access(
        request.role,
        request.resource,
        request.action,
        request.rbac
    )

    return {
        "can_access": result
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)