"""
Servicio enfocado en ajustar el inventario de una determinada tienda después de que
se ha realizado alguna operación como compra, venta, o recuento de inventario.
"""
from abc import ABC, abstractmethod

from domain.entity import AdjustmentProducts, NewProducts, SKU


class InventoryAdjustmentServicePort(ABC):

    @abstractmethod
    def delete_products(self, store_id: int, skus: list[SKU]): pass

    @abstractmethod
    def add_products(self, store_id: int, products: list[NewProducts]) -> None: pass

    @abstractmethod
    def adjust_inventory(self, store_id: int, products: list[AdjustmentProducts]) -> None: pass
