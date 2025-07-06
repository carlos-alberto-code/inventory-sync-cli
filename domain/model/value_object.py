import re
from decimal import Decimal
from dataclasses import dataclass


@dataclass
class SKU:
    value: str

    def __post_init__(self):
        if not self.value:
            raise ValueError("El valor del SKU no puede estar vacío")

        if not self.value.strip():
            raise ValueError("El SKU no puede contener solo espacios en blanco")

        if len(self.value) > 50:
            raise ValueError("El valor del SKU no puede exceder los 50 caracteres")

        if len(self.value) < 3:
            raise ValueError("El SKU debe tener al menos 3 caracteres")

        # Validar formato alfanumérico con guiones y guiones bajos permitidos
        if not re.match(r'^[A-Za-z0-9_-]+$', self.value):
            raise ValueError("El SKU solo puede contener letras, números, guiones y guiones bajos")

        # Validar que no empiece ni termine con guiones o guiones bajos
        if self.value.startswith(('-', '_')) or self.value.endswith(('-', '_')):
            raise ValueError("El SKU no puede empezar ni terminar con guiones o guiones bajos")

        # Normalizar a mayúsculas para consistencia
        self.value = self.value.upper()


@dataclass
class Money:
    value: str

    def __post_init__(self):
        if not self.value:
            raise ValueError("El valor del dinero no puede estar vacío")

        if not re.match(r'^\d+(\.\d{1,2})?$', self.value):
            raise ValueError("El valor del dinero debe ser un número válido con hasta dos decimales")

        # Usar Decimal para precisión en operaciones monetarias
        self._decimal_value = Decimal(self.value)
        self.value = f"{float(self.value):.2f}"

    @staticmethod
    def _get_decimal_value(other: 'Money' | int | float) -> Decimal:
        """Convierte el valor a Decimal para operaciones precisas"""
        if isinstance(other, Money):
            return other._decimal_value
        return Decimal(str(other))

    @staticmethod
    def _create_money_from_decimal(decimal_value: Decimal) -> 'Money':
        """Crea un nuevo objeto Money desde un Decimal"""
        return Money(f"{decimal_value:.2f}")

    # Métodos de comparación
    def __eq__(self, other: 'Money' | int | float) -> bool:
        return self._decimal_value == self._get_decimal_value(other)

    def __lt__(self, other: 'Money' | int | float) -> bool:
        return self._decimal_value < self._get_decimal_value(other)

    def __le__(self, other: 'Money' | int | float) -> bool:
        return self._decimal_value <= self._get_decimal_value(other)

    def __gt__(self, other: 'Money' | int | float) -> bool:
        return self._decimal_value > self._get_decimal_value(other)

    def __ge__(self, other: 'Money' | int | float) -> bool:
        return self._decimal_value >= self._get_decimal_value(other)

    # Métodos de operaciones matemáticas
    def __add__(self, other: 'Money' | int | float) -> 'Money':
        result = self._decimal_value + self._get_decimal_value(other)
        return self._create_money_from_decimal(result)

    def __radd__(self, other: int | float) -> 'Money':
        return self.__add__(other)

    def __sub__(self, other: 'Money' | int | float) -> 'Money':
        result = self._decimal_value - self._get_decimal_value(other)
        return self._create_money_from_decimal(result)

    def __rsub__(self, other: int | float) -> 'Money':
        result = Decimal(str(other)) - self._decimal_value
        return self._create_money_from_decimal(result)

    def __mul__(self, other: 'Money' | int | float) -> 'Money':
        result = self._decimal_value * self._get_decimal_value(other)
        return self._create_money_from_decimal(result)

    def __rmul__(self, other: int | float) -> 'Money':
        return self.__mul__(other)

    def __truediv__(self, other: 'Money' | int | float) -> 'Money':
        other_decimal = self._get_decimal_value(other)
        if other_decimal == 0:
            raise ValueError("No se puede dividir por cero")
        result = self._decimal_value / other_decimal
        return self._create_money_from_decimal(result)

    def __rtruediv__(self, other: int | float) -> 'Money':
        if self._decimal_value == 0:
            raise ValueError("No se puede dividir por cero")
        result = Decimal(str(other)) / self._decimal_value
        return self._create_money_from_decimal(result)