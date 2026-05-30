class CustomerService:

    def classify_customer(self, total_spent: int) -> str:
        """
        Output:
            normal / silver / gold
        """
        pass


def classify_customer_api(total_spent: int) -> dict:
    service = CustomerService()

    customer_type = service.classify_customer(total_spent)

    return {
        "success": True,
        "customer_type": customer_type
    }