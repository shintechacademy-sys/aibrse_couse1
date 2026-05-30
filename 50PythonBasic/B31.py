class CustomerService:

    def find_customer(
        self,
        customers: list[dict],
        phone: str
    ) -> dict | None:
        """
        Output:
            khách hàng có số điện thoại tương ứng
            None nếu không tìm thấy
        """
        pass


def find_customer_api(
    customers: list[dict],
    phone: str
) -> dict:
    service = CustomerService()

    result = service.find_customer(customers, phone)

    return {
        "success": True,
        "data": result
    }