class OrderService:

    def latest_order(self, orders: list[dict]) -> dict | None:
        """
        Output:
            đơn hàng có id lớn nhất
            None nếu danh sách rỗng
        """
        pass


def latest_order_api(orders: list[dict]) -> dict:
    service = OrderService()

    result = service.latest_order(orders)

    return {
        "success": True,
        "data": result
    }