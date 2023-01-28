import psycopg2
from database.db import database


def healthcheck_postgres() -> bool:
    try:
        conn = psycopg2.connect(database.get_db_uri())
        conn.close()
    except psycopg2.OperationalError as op_err:
        print(f"Connection failed: {op_err}")
        return False
    else:
        return True
