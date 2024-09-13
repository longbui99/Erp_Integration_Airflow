from pydantic import BaseModel, Field, EmailStr


class AccountAnalyticLine(BaseModel):
    email: EmailStr = Field(default='account@example.com')
    