from abc import ABC, abstractmethod

from domain.model.model import Sale


class SalesRegistrationServicePort(ABC):

    @abstractmethod
    def record_sale(self, sale: Sale): pass
