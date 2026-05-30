class OrderService:

  def order_message(self, status: str) -> str:
    """
    Input:
        status

    Output:
        thông báo trạng thái
    """
    pass


def order_status_api(status: str) -> dict:
  service = OrderService()

  message = service.order_message(status)

  return {
    "success": True,
    "message": message
  }