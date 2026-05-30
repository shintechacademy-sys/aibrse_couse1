class InventoryService:

    def update_stock(
        self,
        stock: int,
        sold_quantity: int
    ) -> int | str:
        """
        Output:
            - tồn kho mới nếu đủ hàng
            - "Không đủ hàng" nếu bán vượt tồn kho
        """
        pass