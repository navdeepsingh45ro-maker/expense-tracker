print("MAIN FILE STARTED")
from fastapi import FastAPI
from database import engine, Base
from models.user_model import User
from routes.user_routes import router
from models.expense_model import Expense

app = FastAPI()
app.include_router(router)

Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
   return {"message": "Expense Tracker API is running!"} 
