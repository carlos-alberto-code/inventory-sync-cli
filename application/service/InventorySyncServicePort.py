from abc import ABC, abstractmethod


class InventorySyncServicePort(ABC):

    @abstractmethod
    def sync_inventory(self, csv_path: str, store_id: int) -> None:
        pass