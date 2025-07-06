from abc import ABC, abstractmethod

from domain.entity.entity import CSVWarnDataReport


class PDFReportServicePort(ABC):

    @abstractmethod
    def dispatch_pdf_report(self, report_name: str, warn_data: CSVWarnDataReport) -> None:
        """Envía el reporte PDF a través de WhatsApp a una lista de distribución."""
        pass