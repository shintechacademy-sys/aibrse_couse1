class UserService:

    def active_users(self, users: list[dict]) -> list[dict]:
        """
        Output:
            danh sách user đang hoạt động
        """
        pass


def active_users_api(users: list[dict]) -> dict:
    service = UserService()

    result = service.active_users(users)

    return {
        "success": True,
        "data": result
    }