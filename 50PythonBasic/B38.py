from pydantic import BaseModel
from typing import List


class Review(BaseModel):
    rating: float


def average_rating(
    reviews: List[Review]
) -> float:
    """
    TODO:
    Nếu reviews rỗng:
        return 0

    Ngược lại:
        tính trung bình rating.
    """
    pass