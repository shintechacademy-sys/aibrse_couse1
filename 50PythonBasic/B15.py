from fastapi import FastAPI
from pydantic import BaseModel
from typing import List


class User(BaseModel):
    id: int
    name: str
    is_active: bool


def active_users(
    users: List[User]
) -> List[User]:

    result = []

    for user in users:
        # TODO
        pass

    return result


app = FastAPI(title="Bai 15")


@app.post("/users/active")
def active_users_api(users: List[User]):

    result = active_users(users)

    return {
        "data": result
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)