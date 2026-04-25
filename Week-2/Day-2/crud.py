from sqlalchemy.orm import Session
from models import User

def create_user(db: Session, name: str, age: int):
    user = User(name=name, age=age)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_all_users(db: Session):
    return db.query(User).all()


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def update_full_user(db: Session, user_id: int, name: str, age: int):
    user = get_user(db, user_id)
    if user:
        user.name = name
        user.age = age
        db.commit()
        db.refresh(user)
    return user

def update_partial_user(db: Session, user_id: int, name: str, age: int):
    user = get_user(db, user_id)
    if user:
        if name is not None:
            user.name = name
        if age is not None:
            user.age = age
        db.commit()
        db.refresh(user)
    return user


def delete_user(db: Session, user_id: int):
    user = get_user(db, user_id)
    if user:
        db.delete(user)
        db.commit()
    return user