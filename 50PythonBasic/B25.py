class ProductService:

    def filter_by_category(
        self,
        products: list[dict],
        category: str
    ) -> list[dict]:
        """
        Output:
            danh sách sản phẩm thuộc category
        """
        pass


def filter_by_category_api(
    products: list[dict],
    category: str
) -> dict:
    service = ProductService()

    result = service.filter_by_category(products, category)

    return {
        "success": True,
        "data": result
    }