from typing import List
from datetime import datetime
from sqlalchemy import UniqueConstraint
from sqlmodel import Field, SQLModel, Relationship, create_engine

class Category(SQLModel, table=True):
    """Categorías de productos (ej: Aceites, Filtros, Bujías)"""
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(max_length=50, unique=True, index=True)

    # Relaciones
    products: List["Product"] = Relationship(back_populates="category")


class Unit(SQLModel, table=True):
    """Unidades de medida (ej: Pieza, Litro, Kilogramo)"""
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(max_length=50, unique=True, index=True)
    abbreviation: str | None = Field(default=None, max_length=10)

    # Relaciones
    products: List["Product"] = Relationship(back_populates="unit")


class Store(SQLModel, table=True):
    """Tiendas del negocio"""
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(max_length=50, unique=True, index=True)
    phone: str | None = Field(default=None, max_length=20)

    # Relaciones
    inventories: List["Inventory"] = Relationship(back_populates="store")
    sales: List["Sale"] = Relationship(back_populates="store")
    purchases: List["Purchase"] = Relationship(back_populates="store")
    adjustments: List["Adjustment"] = Relationship(back_populates="store")


class Product(SQLModel, table=True):
    """Catálogo central de productos (todos los productos de todas las tiendas)"""
    id: int | None = Field(default=None, primary_key=True)
    sku: str = Field(max_length=50, unique=True, index=True)
    name: str = Field(max_length=100, index=True)

    # Foreign keys requeridas
    unit_id: int = Field(foreign_key="unit.id", index=True)
    category_id: int = Field(foreign_key="category.id", index=True)

    # Relaciones
    unit: Unit = Relationship(back_populates="products")
    category: Category = Relationship(back_populates="products")
    inventories: List["Inventory"] = Relationship(back_populates="product")
    sales: List["Sale"] = Relationship(back_populates="product")
    purchases: List["Purchase"] = Relationship(back_populates="product")
    adjustments: List["Adjustment"] = Relationship(back_populates="product")


class Inventory(SQLModel, table=True):
    """Estado actual del inventario por producto por tienda"""
    __table_args__ = (
        UniqueConstraint("product_id", "store_id", name="unique_product_store"),
    )

    id: int | None = Field(default=None, primary_key=True)

    # Foreign keys requeridas
    product_id: int = Field(foreign_key="product.id", index=True)
    store_id: int = Field(foreign_key="store.id", index=True)

    # Datos del inventario con validaciones de negocio
    quantity: int = Field(ge=0, default=0)  # No puede ser negativo
    cost: float = Field(gt=0)  # Precio de compra debe ser mayor que 0
    price: float = Field(gt=0)  # Precio de venta debe ser mayor que 0

    # Campos adicionales
    min_stock: int | None = Field(default=None, ge=0)  # Stock mínimo

    # Control de cambios
    last_updated: datetime = Field(default_factory=datetime.utcnow, index=True)

    # Relaciones
    product: Product = Relationship(back_populates="inventories")
    store: Store = Relationship(back_populates="inventories")


class Sale(SQLModel, table=True):
    """Ventas detectadas automáticamente por comparación de inventarios"""
    id: int | None = Field(default=None, primary_key=True)

    # Foreign keys requeridas
    product_id: int = Field(foreign_key="product.id", index=True)
    store_id: int = Field(foreign_key="store.id", index=True)

    # Datos de la venta
    quantity: int = Field(gt=0)  # Cantidad vendida (siempre positiva)
    unit_price: float = Field(gt=0)  # Precio unitario de venta
    total_amount: float = Field(gt=0)  # Total de la venta
    cost_per_unit: float = Field(gt=0)  # Costo unitario del producto

    # Metadatos de la transacción
    detected_at: datetime = Field(default_factory=datetime.utcnow, index=True)

    # Campos calculados
    profit: float | None = Field(default=None)  # Ganancia = (unit_price - cost_per_unit) * quantity

    # Relaciones
    product: Product = Relationship(back_populates="sales")
    store: Store = Relationship(back_populates="sales")


class Purchase(SQLModel, table=True):
    """Compras registradas manualmente en el sistema"""
    id: int | None = Field(default=None, primary_key=True)

    # Foreign keys requeridas
    product_id: int = Field(foreign_key="product.id", index=True)
    store_id: int = Field(foreign_key="store.id", index=True)

    # Datos de la compra
    quantity: int = Field(gt=0)  # Cantidad comprada
    unit_cost: float = Field(gt=0)  # Costo unitario
    total_cost: float = Field(gt=0)  # Costo total

    # Información del proveedor
    supplier_name: str | None = Field(default=None, max_length=100)

    # Metadatos
    purchase_date: datetime = Field(default_factory=datetime.utcnow, index=True)

    # Relaciones
    product: Product = Relationship(back_populates="purchases")
    store: Store = Relationship(back_populates="purchases")


class Adjustment(SQLModel, table=True):
    """Ajustes de inventario por conteos físicos, mermas, correcciones"""
    id: int | None = Field(default=None, primary_key=True)

    # Foreign keys requeridas
    product_id: int = Field(foreign_key="product.id", index=True)
    store_id: int = Field(foreign_key="store.id", index=True)

    # Datos del ajuste
    quantity: int = Field(ge=0)  # Cantidad contada en inventario físico


    # Metadatos
    adjustment_date: datetime = Field(default_factory=datetime.utcnow, index=True)
    performed_by: str | None = Field(default=None, max_length=100)  # Quién hizo el ajuste


    # Relaciones
    product: Product = Relationship(back_populates="adjustments")
    store: Store = Relationship(back_populates="adjustments")
