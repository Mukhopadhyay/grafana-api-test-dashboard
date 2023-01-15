from pydantic import PostgresDsn
from sqlalchemy.orm import Session
from configs import database_config
from sqlalchemy import create_engine

class Database:

    def __init__(self) -> None:
        self.db_uri = PostgresDsn.build(
            scheme="postgresql",
            user=database_config.postgres_user,
            password=database_config.postgres_password,
            host=database_config.postgres_service,
            port=str(database_config.postgres_port),
            path=f"/{database_config.postgres_db}"
        )
        self.__engine = create_engine(self.db_uri)
    
    def get_session(self) -> Session:
        return Session(self.__engine, autocommit=False)

# Singleton class, this is to be used by all modules
database = Database()
