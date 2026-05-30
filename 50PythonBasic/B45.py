from pydantic import BaseModel
from typing import List


class OrderItem(BaseModel):
    product_id: int
    name: str
    qty: int
    price: float


def top_selling(
    items: List[OrderItem],
    top_n: int
) -> List[dict]:
    """
    TODO:
    Gom nhóm theo product_id.

    Với mỗi product_id cần tính:
        - product_id
        - name
        - total_qty
        - revenue

    Sau đó:
        - sắp xếp theo total_qty giảm dần
        - lấy top_n sản phẩm đầu tiên
    """

    summary = {}

    for item in items:
        # TODO:
        # Nếu product_id chưa có trong summary:
        #     tạo dữ liệu ban đầu
        # Nếu đã có:
        #     cộng thêm qty và revenue
        pass

    result = []

    # TODO:
    # Chuyển summary thành list
    # Sắp xếp giảm dần theo total_qty
    # Lấy top_n

    return result