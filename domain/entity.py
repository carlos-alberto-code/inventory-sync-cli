from dataclasses import dataclass


@dataclass
class ProductQuantityWarnReport:
    sku: str
    name: str
    quantity: int
    note: str = 'Corregir cantidad del producto'


@dataclass
class ProductNegativePurchasePriceWarnReport:
    sku: str
    name: str
    purchase_price: float
    note: str = 'Corregir precio de compra del producto'


@dataclass
class ProductNegativeSalePriceWarnReport:
    sku: str
    name: str
    sale_price: float
    note: str = 'Corregir precio de venta del producto'


@dataclass
class ProductSalePriceLessThanPurchaseReport:
    sku: str
    name: str
    purchase_price: float
    sale_price: float
    note: str = 'El precio de venta es menor que el precio de compra del producto'


@dataclass
class CSVWarnDataReport:
    name: str | None
    products_quantities_warns: list[ProductQuantityWarnReport] | None
    products_negative_purchase_prices_warns: list[ProductNegativePurchasePriceWarnReport] | None
    products_negative_sale_prices_warns: list[ProductNegativeSalePriceWarnReport] | None
    products_sale_price_less_than_purchase_warns: list[ProductSalePriceLessThanPurchaseReport] | None


@dataclass
class SKU:
    value: str

    def __post_init__(self):
        if not self.value:
            raise ValueError("SKU cannot be empty")
        if len(self.value) > 50:
            raise ValueError("SKU cannot exceed 50 characters")


@dataclass
class AdjustmentProducts:
    sku: str
    quantity: int
    purchase_price: float
    sale_price: float

    def __post_init__(self):
        if self.quantity < 0:
            raise ValueError("Quantity cannot be negative")
        if self.purchase_price < 0:
            raise ValueError("Purchase price cannot be negative")
        if self.sale_price < 0:
            raise ValueError("Sale price cannot be negative")


@dataclass
class NewProducts:
    sku: str
    name: str
    quantity: int
    purchase_price: float
    sale_price: float

    def __post_init__(self):
        if self.quantity < 0:
            raise ValueError("Quantity cannot be negative")
        if self.purchase_price < 0:
            raise ValueError("Purchase price cannot be negative")
        if self.sale_price < 0:
            raise ValueError("Sale price cannot be negative")
