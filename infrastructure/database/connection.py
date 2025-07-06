import os
from typing import Generator
from dotenv import load_dotenv
from contextlib import contextmanager
from sqlmodel import create_engine, Session


load_dotenv()
SQLITE_DATABASE_URL_PRE = os.getenv("SQLITE_DATABASE_URL_PRE")

if not SQLITE_DATABASE_URL_PRE:
    raise ValueError("La variable de entorno SQLITE_DATABASE_URL_PRE no está definida. Asegúrate de que el archivo .env esté configurado correctamente.")

engine = create_engine(SQLITE_DATABASE_URL_PRE)

@contextmanager
def get_session() -> Generator[Session, None, None]:
    session = Session(engine)
    try:
        yield session
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()
