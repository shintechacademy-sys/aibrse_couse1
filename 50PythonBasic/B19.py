class OrderService:

    def order_code(self, order_id: int) -> str:
        """
        Output:
            mã đơn dạng ORD-00027
        """
        pass


def order_code_api(order_id: int) -> dict:
    service = OrderService()

    code = service.order_code(order_id)

    return {
        "success": True,
        "order_code": code
    }