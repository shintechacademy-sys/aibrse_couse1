from typing import Dict


def apply_coupon(
    cart_total: float,
    code: str,
    coupon_db: Dict[str, dict]
) -> dict:
    """
    TODO:
    Kiểm tra mã giảm giá có hợp lệ không.

    Nếu code không tồn tại:
        return {
            "valid": False,
            "discount_amount": 0,
            "final_price": cart_total,
            "message": "Mã giảm giá không tồn tại"
        }

    Nếu cart_total < min_order:
        return {
            "valid": False,
            "discount_amount": 0,
            "final_price": cart_total,
            "message": "Đơn hàng chưa đủ điều kiện"
        }

    Nếu hợp lệ:
        - type == "percent": giảm theo %
        - type == "fixed": giảm số tiền cố định

    Output:
        {
            "valid": True,
            "discount_amount": ...,
            "final_price": ...,
            "message": "Áp dụng thành công"
        }
    """
    pass