class CustomerSegmentationService:

    def segment_users(self, order_counts: dict) -> dict:
        """
        Output:
            {
                "one_time": set,
                "repeat": set,
                "vip": set
            }
        """
        pass


def segment_users_api(order_counts: dict) -> dict:
    service = CustomerSegmentationService()
    result = service.segment_users(order_counts)

    return {
        "success": True,
        "data": result
    }