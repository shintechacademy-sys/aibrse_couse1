from fastapi import FastAPI
from pydantic import BaseModel


class NormalizeNameRequest(BaseModel):
    name: str


def normalize_name(name: str) -> str:
    """
    TODO:
    Xóa khoảng trắng đầu cuối.
    Viết hoa chữ cái đầu mỗi từ.
    """
    pass


app = FastAPI(title="Bai 27")


@app.post("/users/normalize-name")
def normalize_name_api(request: NormalizeNameRequest):
    result = normalize_name(request.name)

    return {
        "normalized_name": result
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)