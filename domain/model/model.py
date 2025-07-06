from dataclasses import dataclass

from domain.model.value_object import SKU, Money


@dataclass
class Category:
    id: int
    name: str

    def __post_init__(self):
        if not self.name:
            raise ValueError("El nombre de la categoría no puede estar vacío")
        if len(self.name) > 100:
            raise ValueError("El nombre de la categoría no puede exceder los 100 caracteres")
        self.name = self.name.strip().upper()


@dataclass
class Unit:
    id: int
    name: str

    def __post_init__(self):
        if not self.name:
            raise ValueError("El nombre de la unidad no puede estar vacío")
        if len(self.name) > 50:
            raise ValueError("El nombre de la unidad no puede exceder los 50 caracteres")
        self.name = self.name.strip().upper()


@dataclass
class Product:
    sku: SKU
    unit_id: int
    category_id: int
    name: str
    quantity: int
    purchase_price: Money
    sale_price: Money

    def __post_init__(self):
        if self.quantity < 0:
            raise ValueError("La cantidad del producto no puede ser negativa")
        if self.sale_price < self.purchase_price:
            raise ValueError("El precio de venta no puede ser menor que el precio de compra")
        if not self.name:
            raise ValueError("El nombre del producto no puede estar vacío")
        if len(self.name) > 100:
            raise ValueError("El nombre del producto no puede exceder los 100 caracteres")
        self.name = self.name.strip().upper()
        if self.category_id < 0 or self.category_id == 0:
            raise ValueError("El ID de la categoría no puede ser cero ni negativo")
        if self.unit_id < 0 or self.unit_id == 0:
            raise ValueError("El ID de la unidad no puede ser cero ni negativo")
