from database.db import database
from models import apis

def insert_into_endpoint(data: apis.Endpoint):
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
                session.execute('TRUNCATE TABLE endpoint;')
            except Exception as err:
                print(err)
                session.rollback()
                return {"msg": "Couldn't truncate table"}
            else:
                session.commit()
                return {"msg": "Table truncated"}
