from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database_config import SessionLocal
from models import User


router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def login(username: str, password: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.user_name == username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User Not Exist")
    if not user.user_password == password:
        raise HTTPException(status_code=404, detail="User Password Is Invalid")
    return user
