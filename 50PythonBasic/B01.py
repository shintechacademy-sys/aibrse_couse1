class ProductService:

    def filter_available(self, products: list[dict]) -> list[dict]:
        """
        Input:
            products: danh sách sản phẩm

        Output:
            danh sách sản phẩm còn hàng và đang active
        """
        pass


def get_available_products_api(products: list[dict]) -> dict:
    """
    API Input:
        products

    API Output:
        {
            "success": True,
            "data": [...]
        }
    """
    service = ProductService()

    result = service.filter_available(products)

    return {
        "success": True,
        "data": result
    }