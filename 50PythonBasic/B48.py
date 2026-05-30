class FlashSaleService:

    def sale_diff(
        self,
        old_sale: set[str],
        new_sale: set[str]
    ) -> dict:
        """
        Output:
            {
                "removed": set,
                "added": set,
                "kept": set
            }
        """
        pass


def sale_diff_api(
    old_sale: set[str],
    new_sale: set[str]
) -> dict:
    service = FlashSaleService()
    result = service.sale_diff(old_sale, new_sale)

    return {
        "success": True,
        "data": result
    }