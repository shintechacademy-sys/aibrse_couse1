class RevenueService:

    def daily_revenue(self, transactions: list[dict]) -> int:
        """
        Output:
            tổng amount của giao dịch success
        """
        pass


def daily_revenue_api(transactions: list[dict]) -> dict:
    service = RevenueService()

    total = service.daily_revenue(transactions)

    return {
        "success": True,
        "revenue": total
    }