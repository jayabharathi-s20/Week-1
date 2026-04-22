from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# -------------------------
# Fake database (in-memory)
# -------------------------
users = {
    1: {"name": "Alice", "age": 25},
    2: {"name": "Bob", "age": 30}
}

# -------------------------
# Pydantic model
# -------------------------
class User(BaseModel):
    name: str
    age: int


# -------------------------
# 1. GET routes
# -------------------------
@app.get("/")
def home():
    return {"message": "Welcome to FastAPI"}


@app.get("/hello")
def hello():
    return {"message": "Hello World"}


@app.get("/users/{user_id}")
def get_user(user_id: int):
    return users.get(user_id, {"error": "User not found"})


@app.get("/items/")
def get_items(limit: int = 5):
    return {"limit": limit, "items": list(range(limit))}


# -------------------------
# 2. POST (Create user)
# -------------------------
@app.post("/users/{user_id}")
def create_user(user_id: int, user: User):
    if user_id in users:
        return {"error": "User already exists"}

    users[user_id] = user.dict()
    return {"message": "User created", "user": users[user_id]}


# -------------------------
# 3. PUT (Replace full user)
# -------------------------
@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):
    users[user_id] = user.dict()
    return {"message": "User fully updated", "user": users[user_id]}


# -------------------------
# 4. PATCH (Partial update)
# -------------------------
@app.patch("/users/{user_id}")
def patch_user(user_id: int, user: dict):
    if user_id not in users:
        return {"error": "User not found"}

    users[user_id].update(user)
    return {"message": "User partially updated", "user": users[user_id]}


# -------------------------
# 5. DELETE (optional but useful)
# -------------------------
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    if user_id in users:
        del users[user_id]
        return {"message": "User deleted"}

    return {"error": "User not found"}