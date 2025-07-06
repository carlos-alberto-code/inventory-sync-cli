from domain.entity.entity import CSVWarnDataReport
from domain.service.PDFRepotServicePort import PDFReportServicePort


class PDFReportServiceCore(PDFReportServicePort):

    def dispatch_pdf_report(self, report_name: str, warn_data: CSVWarnDataReport) -> None:
        """Envía el reporte PDF a través de WhatsApp a una lista de distribución."""
        # Aquí se implementaría la lógica para enviar el reporte PDF por WhatsApp.
        # Por ejemplo, utilizando una API de WhatsApp Business o un servicio similar.
        print(f"Enviando reporte PDF '{report_name}' por WhatsApp.")
        # Implementación específica del envío del reporte
        # ...
