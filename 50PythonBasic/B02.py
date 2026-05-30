class CartService:

    def cart_total(self, cart: list[dict]) -> int:
        """
        Input:
            cart

        Output:
            tổng tiền
        """
        pass


def cart_total_api(cart: list[dict]) -> dict:
    service = CartService()

    total = service.cart_total(cart)

    return {
        "success": True,
        "total": total
    }