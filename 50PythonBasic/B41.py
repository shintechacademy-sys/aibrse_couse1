class CatalogService:

    def build_catalog(self, products: list[dict]) -> dict:
        """
        Output:
            dict dạng {id: product_info}
            nếu trùng id thì giữ sản phẩm sau cùng
        """
        pass


def build_catalog_api(products: list[dict]) -> dict:
    service = CatalogService()
    result = service.build_catalog(products)

    return {
        "success": True,
        "data": result
    }