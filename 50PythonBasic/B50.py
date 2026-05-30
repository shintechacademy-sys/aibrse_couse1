class CampaignService:

    def check_conflicts(
        self,
        flash_sale_items: set[str],
        active_campaigns: dict
    ) -> dict:
        """
        Output:
            {
                "has_conflict": bool,
                "conflicts": {
                    product_id: [campaign_name]
                },
                "safe_items": set
            }
        """
        pass


def check_conflicts_api(
    flash_sale_items: set[str],
    active_campaigns: dict
) -> dict:
    service = CampaignService()
    result = service.check_conflicts(
        flash_sale_items,
        active_campaigns
    )

    return {
        "success": True,
        "data": result
    }