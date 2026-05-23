from pydantic import BaseModel, Field

class ExpenseCreate(BaseModel):
    amount: float = Field(..., gt=0, description="The amount of the expense")
    category: str = Field(..., description="The category of the expense")
    note: str | None = Field(None, description="A note about the expense")