from abc import ABC, abstractmethod

from domain.entity.entity import CSVWarnDataReport, ProductQuantityWarnReport, ProductNegativePurchasePriceWarnReport, \
    ProductNegativeSalePriceWarnReport, ProductSalePriceLessThanPurchaseReport


class InventoryValidationServicePort(ABC):

    @abstractmethod
    def get_warn_data(self) -> CSVWarnDataReport: pass

    @abstractmethod
    def is_csv_file_valid(self) -> bool: pass

    @abstractmethod
    def validate(self) -> None: pass

    @abstractmethod
    def get_products_with_negative_quantities(self) -> list[ProductQuantityWarnReport]: pass

    @abstractmethod
    def get_products_with_negative_purchase_prices(self) -> list[ProductNegativePurchasePriceWarnReport]: pass

    @abstractmethod
    def get_products_with_negative_sale_prices(self) -> list[ProductNegativeSalePriceWarnReport]: pass

    @abstractmethod
    def get_products_with_sale_price_less_than_purchase(self) -> list[ProductSalePriceLessThanPurchaseReport]: pass
