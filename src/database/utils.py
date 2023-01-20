import psycopg2

from database.db import database
from models import response


def insert_into_endpoint(data: response.Response):
    with database.get_session() as session:
        with session.begin():
            try:
                session.add(data)
            except Exception as err:
                print(err)
                session.rollback()
                return {"msg": "Couldn't insert into database"}
            else:
                session.commit()
                return {"msg": "Data insert"}


def truncate_endpoint_tbl():
    with database.get_session() as session:
        with session.begin():
            try:
                session.execute("TRUNCATE TABLE endpoint;")
            except Exception as err:
                print(err)
                session.rollback()
                return {"msg": "Couldn't truncate table"}
            else:
                session.commit()
                return {"msg": "Table truncated"}


def healthcheck_postgres() -> bool:
    try:
        conn = psycopg2.connect(database.get_db_uri())
        conn.close()
    except psycopg2.OperationalError as op_err:
        print(f"Connection failed: {op_err}")
        return False
    else:
        return True
