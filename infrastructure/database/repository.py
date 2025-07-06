from sqlmodel import select
from sqlmodel import SQLModel
from typing import TypeVar, Generic
from infrastructure.database.connection import get_session


T = TypeVar('T', bound=SQLModel)


class Repository(Generic[T]):

    def __init__(self, model: type[T]):
        super().__init__()
        self._model = model

    @staticmethod
    def create(entity: T) -> T:
        try:
            with get_session() as session:
                session.add(entity)
                session.commit()
                session.refresh(entity)
                return entity
        except Exception as e:
            raise Exception(f"Error al crear la entidad: {e}")

    @staticmethod
    def create_all(entities: list[T]) -> list[T]:
        try:
            with get_session() as session:
                session.add_all(entities)
                session.commit()
                for entity in entities:
                    session.refresh(entity)
                return entities
        except Exception as e:
            raise Exception(f"Error al crear las entidades: {e}")

    def get_by_id(self, entity_id: int) -> T | None:
        try:
            with get_session() as session:
                return session.get(self._model, entity_id)
        except Exception as e:
            raise Exception(f"Error al obtener la entidad mediante el id: {e}")

    def get_all(self) -> list[T]:
        try:
            with get_session() as session:
                statement = select(self._model)
                result = session.exec(statement)
                return list(result.all())
        except Exception as e:
            raise Exception(f"Error al obtener todas las entidades: {e}")

    @staticmethod
    def update(entity: T) -> T:
        try:
            with get_session() as session:
                updated_entity = session.merge(entity)
                session.commit()
                session.refresh(updated_entity)
                return updated_entity
        except Exception as e:
            raise Exception(f"Error al actualizar la entidad: {e}")
