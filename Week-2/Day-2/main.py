from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import session_creation
import crud

app = FastAPI()

def get_db():
    db = session_creation()
    try:
        yield db
    finally:
        db.close()

@app.post("/users")
def create_user(name: str, age: int, db: Session = Depends(get_db)):
    return crud.create_user(db, name, age)

@app.get("/users")
def read_users(db: Session = Depends(get_db)):
    return crud.get_all_users(db)

@app.get("/users/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_db)):
    return crud.get_user(db, user_id)

@app.put("/users/{user_id}")
def update_user(user_id: int, name: str, age: int, db: Session = Depends(get_db)):
    return crud.update_full_user(db, user_id, name, age)

@app.patch("/users/{user_id}")
def patch_user(user_id: int, name: str = None, age: int = None, db: Session = Depends(get_db)):
    return crud.update_partial_user(db, user_id, name, age)

@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return crud.delete_user(db, user_id)