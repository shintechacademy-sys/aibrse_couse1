class CouponService:

    def coupon_exists(
        self,
        code: str,
        coupons: list[str]
    ) -> bool:
        """
        Output:
            True nếu code tồn tại trong coupons
        """
        pass


def coupon_exists_api(code: str, coupons: list[str]) -> dict:
    service = CouponService()

    exists = service.coupon_exists(code, coupons)

    return {
        "success": True,
        "exists": exists
    }