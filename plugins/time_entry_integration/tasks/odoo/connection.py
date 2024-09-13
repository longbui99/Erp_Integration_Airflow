import xmlrpc.client
import typing

from pydantic import BaseModel, Field


class XMLRPC(BaseModel):
    base_url: str
    username: str
    password: str
    database: str
    uid: typing.Optional[str] = None
    model: typing.Optional[str] = None

    def init_connection(self):
        common = xmlrpc.client.ServerProxy(f'{self.base_url}/xmlrpc/2/common')
        common.version()
        self.uid = common.authenticate(self.database, self.username, self.password, {})
        model = xmlrpc.client.ServerProxy(f'{self.base_url}/xmlrpc/2/object')
        self.model = model

    def load(self, *args, **kwargs):
        return self.model.execute_kw(self.database, self.uid, self.password, *args, **kwargs)


def init_odoo_connection():
    obj = XMLRPC(base_url='https://staging.rslve.novobi.com', username="admin", password="Novobi@2024", database='stag_prod_082724')
    obj.init_connection()
    return obj
