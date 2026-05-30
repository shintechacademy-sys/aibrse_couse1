class ProductService:

    def cheapest_product(self, products: list[dict]) -> dict | None:
        """
        Output:
            sản phẩm có price nhỏ nhất
            None nếu danh sách rỗng
        """
        pass


def cheapest_product_api(products: list[dict]) -> dict:
    service = ProductService()

    result = service.cheapest_product(products)

    return {
        "success": True,
        "data": result
    }