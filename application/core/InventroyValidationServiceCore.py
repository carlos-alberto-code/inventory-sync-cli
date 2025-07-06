import os
from pandas import DataFrame, read_csv

from domain.entity.entity import CSVWarnDataReport, ProductSalePriceLessThanPurchaseReport, \
    ProductNegativeSalePriceWarnReport, ProductQuantityWarnReport, ProductNegativePurchasePriceWarnReport
from domain.service.InventoryValidationServicePort import InventoryValidationServicePort


class InventoryValidationServiceCore(InventoryValidationServicePort):

    def __init__(self, csv_path: str):
        super().__init__()
        self._csv_path = csv_path
        self._used_columns = [
            'Clave', 'Unidad', 'Nombre de producto', 'Cantidad',
            'Precio de compra', 'Precio de venta', 'Categoría'
        ]
        self._dataframe = read_csv(csv_path, usecols=self._used_columns)
        self._csv_warn_data_report = CSVWarnDataReport(name='Reporte de advertencias')

    def get_products_with_negative_purchase_prices(self) -> list[ProductNegativePurchasePriceWarnReport]:
        pass

    def get_products_with_negative_quantities(self) -> list[ProductQuantityWarnReport]:
        pass

    def get_products_with_negative_sale_prices(self) -> list[ProductNegativeSalePriceWarnReport]:
        pass

    def get_products_with_sale_price_less_than_purchase(self) -> list[ProductSalePriceLessThanPurchaseReport]:
        pass

    def get_warn_data(self) -> CSVWarnDataReport:
        return self._csv_warn_data_report

    def is_csv_file_valid(self) -> bool:
        self.validate()
        self._csv_warn_data_report.products_quantities_warns = self.get_products_with_negative_quantities()
        self._csv_warn_data_report.products_negative_purchase_prices_warns = self.get_products_with_negative_purchase_prices()
        self._csv_warn_data_report.products_negative_sale_prices_warns = self.get_products_with_negative_sale_prices()
        self._csv_warn_data_report.products_sale_price_less_than_purchase_warns = self.get_products_with_sale_price_less_than_purchase()
        return not (
            self._csv_warn_data_report.products_quantities_warns or
            self._csv_warn_data_report.products_negative_purchase_prices_warns or
            self._csv_warn_data_report.products_negative_sale_prices_warns or
            self._csv_warn_data_report.products_sale_price_less_than_purchase_warns
        )

    def validate(self):
        if not os.path.exists(self._csv_path):
            raise FileNotFoundError(f"El archivo CSV '{self._csv_path}' no existe.")

        if self._dataframe.empty:
            raise ValueError("El archivo CSV está vacío o no contiene datos válidos.")

        if not all(column in self._dataframe.columns for column in self._used_columns):
            raise ValueError(f"El archivo CSV debe contener las siguientes columnas: {', '.join(self._used_columns)}")
