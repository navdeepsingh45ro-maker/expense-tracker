from fastapi import APIRouter, HTTPException
from schemas.user_schema import UserCreate
from models.user_model import User
from database import SessionLocal
from auth.hashing import hash_password

router = APIRouter()
@router.post("/users/")
def create_user(user: UserCreate):

    db = SessionLocal()
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already exists")
    
    hashed_password = hash_password(user.password)
    new_user = User(email=user.email,password=hashed_password)
    db.add(new_user)
    db.commit()
    return {"message": "User created successfully"}