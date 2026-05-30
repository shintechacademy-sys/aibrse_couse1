class ReportService:

    def daily_report(self, transactions: list[dict]) -> dict:
        """
        Output:
            {
                "2024-01-15": {
                    "total": ...,
                    "count": ...,
                    "avg": ...
                }
            }
        """
        pass


def daily_report_api(transactions: list[dict]) -> dict:
    service = ReportService()
    result = service.daily_report(transactions)

    return {
        "success": True,
        "data": result
    }