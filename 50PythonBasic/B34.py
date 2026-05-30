from pydantic import BaseModel
from typing import List


class Transaction(BaseModel):
    type: str
    amount: float


def refund_total(
    transactions: List[Transaction]
) -> float:
    """
    TODO:
    Tính tổng amount của các transaction có type là "refund".
    """

    total = 0

    for transaction in transactions:
        # TODO
        pass

    return total