class UserService:

    def normalize_name(self, name: str) -> str:
        """
        Output:
            tên đã xóa khoảng trắng thừa và viết hoa chữ cái đầu mỗi từ
        """
        pass


def normalize_name_api(name: str) -> dict:
    service = UserService()

    result = service.normalize_name(name)

    return {
        "success": True,
        "normalized_name": result
    }