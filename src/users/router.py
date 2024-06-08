from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from . import models, schemas
from ..utils import get_password_hash, verify_password, create_api_key
from ..logging_config import user_logger

router = APIRouter()

@router.post("/register", response_model=schemas.UserResponse)
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    user_logger.info(f"Attempting to register user with phone number: {hash(user.phone_number)}")
    db_user = db.query(models.User).filter(models.User.phone_number == user.phone_number).first()
    if db_user:
        user_logger.warning(f"Phone number already registered: {hash(user.phone_number)}")
        raise HTTPException(status_code=400, detail="Phone number already registered")
    
    hashed_password = get_password_hash(user.password)
    api_key = create_api_key()
    new_user = models.User(
        first_name=user.first_name,
        last_name=user.last_name,
        phone_number=user.phone_number,
        hashed_password=hashed_password,
        api_key=api_key
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    user_logger.info(f"User registered successfully: {new_user.id}")
    return new_user

@router.post("/auth", response_model=schemas.UserResponse)
def authenticate_user(user: schemas.UserAuth, db: Session = Depends(get_db)):
    user_logger.info(f"User attempting to authenticate with phone number: {hash(user.phone_number)}")
    db_user = db.query(models.User).filter(models.User.phone_number == user.phone_number).first()
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        user_logger.warning(f"Authentication failed for user with phone number: {hash(user.phone_number)}")
        raise HTTPException(status_code=400, detail="Invalid phone number or password")
    user_logger.info(f"User authenticated successfully: {db_user.id}")
    return db_user
