from fastapi import APIRouter, HTTPException, Depends
from schemas.user_schema import UserCreate
from models.user_model import User
from database import SessionLocal
from auth.hashing import hash_password
from schemas.login_schema import LoginSchema
from auth.hashing import verify_password
from auth.jwt_handler import create_access_token
from sqlalchemy.orm import Session
from database import get_db
 


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

@router.post("/login")
def login(request: LoginSchema, db: Session = Depends(get_db)):

    user = db.query(User).filter(User.email == request.email).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if not verify_password(request.password, user.password):
        raise HTTPException(status_code=401, detail="Incorrect password")

    access_token = create_access_token(data={"user_id": user.id})

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
