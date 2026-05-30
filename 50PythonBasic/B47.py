class RbacService:

    def can_access(
        self,
        role: str,
        resource: str,
        action: str,
        rbac: dict
    ) -> bool:
        """
        Output:
            True nếu role có quyền action trên resource
        """
        pass


def can_access_api(
    role: str,
    resource: str,
    action: str,
    rbac: dict
) -> dict:
    service = RbacService()
    result = service.can_access(role, resource, action, rbac)

    return {
        "success": True,
        "can_access": result
    }