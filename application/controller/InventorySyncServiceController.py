from application.service.SenderServicePort import SenderServicePort
from application.service.PDFRepotServicePort import PDFReportServicePort
from application.service.InventorySyncServicePort import InventorySyncServicePort
from application.service.InventoryValidationServicePort import InventoryValidationServicePort


class InventorySyncServiceController:
    """
    Esta clase recibe las dependencias (clases o instancias) necesarias para realizar trabajo. Internamente, orquesta las cosas para que se ejecute el objetivo de la aplicación.
    """

    def __init__(
        self,
        csv_path: str,
        store_id: int,
        sender_service: SenderServicePort,
        report_service: PDFReportServicePort,
        inventory_sync_service: InventorySyncServicePort,
        inventory_validation_service: InventoryValidationServicePort,

    ) -> None:
        self._csv_path = csv_path
        self._store_id = store_id
        self._sender_service = sender_service
        self._report_service = report_service
        self._inventory_sync_service = inventory_sync_service
        self._inventory_validation_service = inventory_validation_service

    def sync(self) -> None:
        if self._inventory_validation_service.is_csv_file_valid():
            self._inventory_sync_service.sync_inventory(csv_path=self._csv_path, store_id=1)
        else:
            warn_data = self._inventory_validation_service.get_warn_data()
            self._report_service.dispatch_pdf_report('Reporte de advertencias', warn_data)
