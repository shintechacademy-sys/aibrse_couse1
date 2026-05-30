class WishlistService:

    def is_wishlisted(
        self,
        product_id: str,
        wishlist: set[str]
    ) -> bool:
        """
        Output:
            True nếu sản phẩm nằm trong wishlist
        """
        pass


def is_wishlisted_api(
    product_id: str,
    wishlist: set[str]
) -> dict:
    service = WishlistService()

    result = service.is_wishlisted(
        product_id,
        wishlist
    )

    return {
        "success": True,
        "is_wishlisted": result
    }