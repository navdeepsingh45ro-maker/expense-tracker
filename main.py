from fastapi import FastAPI
from database import engine, Base
from models.user_model import User
from routes.user_routes import router

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(router)

@app.get("/")
def home():
   return {"message": "Expense Tracker API is running!"} 