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
