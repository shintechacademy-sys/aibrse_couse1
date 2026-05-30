class AnalyticsService:

    def top_selling(
        self,
        items: list[dict],
        top_n: int
    ) -> list[dict]:
        """
        Output:
            danh sách top_n sản phẩm theo total_qty giảm dần

            Mỗi phần tử có dạng:
            {
                "product_id": ...,
                "name": ...,
                "total_qty": ...,
                "revenue": ...
            }
        """
        pass