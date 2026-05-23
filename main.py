
from fastapi import FastAPI
from database import engine, Base
from models.user_model import User
from routes.user_routes import router
from models.expense_model import Expense
from routes.expense_routes import router as expense_router
from routes.budget_routes import router as budget_router

app = FastAPI()
app.include_router(router)
app.include_router(expense_router)
app.include_router(budget_router)

Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
   return {"message": "Expense Tracker API is running!"} 
