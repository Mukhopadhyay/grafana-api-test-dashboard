from database.crud import base
from models import models


class ApiCRUD(base.CRUDBase):
    def __init__(self):
        super().__init__(models.Api)
