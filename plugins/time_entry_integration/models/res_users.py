from typing import List
from pydantic import BaseModel, Field, EmailStr, TypeAdapter
from time_entry_integration.tasks.odoo.connection import init_odoo_connection

class ResUsers(BaseModel):
    email: str
    id: int
    login: str


def load_user(domain, **kwargs):
    connection = init_odoo_connection()
    kwargs['fields'] = ['login', 'email', 'id']
    users = connection.load('res.users', 'search_read', domain, kwargs)
    ta = TypeAdapter(List[ResUsers])
    res = ta.validate_python(users)
    return res
