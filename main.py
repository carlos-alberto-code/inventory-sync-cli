from application.core.PDFReportServiceCore import PDFReportServiceCore
from application.core.InventorySyncServiceCore import InventorySyncServiceCore
from application.core.InventroyValidationServiceCore import InventoryValidationServiceCore
from application.controller.InventorySyncServiceController import InventorySyncServiceController
from infrastructure.adapter.WhatsappSenderServiceAdapter import WhatsappSenderServiceAdapter

csv_file_path = 'inventory.csv'

inventory_sync_service_controller = InventorySyncServiceController(
    csv_path=csv_file_path,
    store_id=1,
    report_service=PDFReportServiceCore(),
    sender_service=WhatsappSenderServiceAdapter(),
    inventory_sync_service=InventorySyncServiceCore(),
    inventory_validation_service=InventoryValidationServiceCore(csv_file_path),
)

inventory_sync_service_controller.sync()
