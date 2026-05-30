class RecommendationService:

    def related_products(
        self,
        product_id: int,
        products: list[dict],
        limit: int
    ) -> list[dict]:
        """
        Output:
            danh sách sản phẩm cùng category,
            không bao gồm sản phẩm hiện tại,
            sắp xếp rating giảm dần
        """
        pass


def related_products_api(
    product_id: int,
    products: list[dict],
    limit: int
) -> dict:
    service = RecommendationService()
    result = service.related_products(product_id, products, limit)

    return {
        "success": True,
        "data": result
    }