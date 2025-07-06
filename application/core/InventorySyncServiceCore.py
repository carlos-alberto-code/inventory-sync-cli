from domain.service.InventorySyncServicePort import InventorySyncServicePort


class InventorySyncServiceCore(InventorySyncServicePort):

    def sync_inventory(self, csv_path: str, store_id: int) -> None:
        ...