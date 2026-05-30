class CouponService:

    def apply_coupon(
        self,
        cart_total: float,
        code: str,
        coupon_db: dict
    ) -> dict:
        """
        Output:
            {
                "valid": bool,
                "discount_amount": number,
                "final_price": number,
                "message": str
            }
        """
        pass