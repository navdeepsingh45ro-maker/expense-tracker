from pydantic import BaseModel

class ExpenseCreate(BaseModel):
    amount: float
    category: str
    note: str