class FraudDetectionService:

    def detect_anomalies(
        self,
        orders: list[dict],
        threshold: float
    ) -> list[dict]:
        """
        Output:
            danh sách đơn hàng có total > threshold * avg
            nếu danh sách rỗng trả về []
        """
        pass


def detect_anomalies_api(
    orders: list[dict],
    threshold: float
) -> dict:
    service = FraudDetectionService()
    result = service.detect_anomalies(orders, threshold)

    return {
        "success": True,
        "data": result
    }