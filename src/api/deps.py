from typing import Generator

from database.db import database


def get_db() -> Generator:
    try:
        session = database.get_db()
        yield session
    finally:
        session.close()
