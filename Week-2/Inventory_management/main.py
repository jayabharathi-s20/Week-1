from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Item, Category
import crud
from datetime import date, timedelta
from sqlalchemy import func

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users")
def create_user(name: str, email: str, db: Session = Depends(get_db)):
    """
    To create new user.
    Parameters:
        name:name of the user
        email:email of the user
    Returns:
        Created user object
    """
    try:
        return crud.create_user(db, {"name": name, "email": email})
    except Exception as e:
        raise HTTPException(500, str(e))


@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    """
    Retrieve all users.
    """
    try:
        return crud.get_users(db)
    except Exception as e:
        raise HTTPException(500, str(e))


@app.get("/users/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    """
    Get a single user by ID.
    Parameters:
        user_id:ID of the user
    """
    try:
        user = crud.get_user(db, user_id)
        if not user:
            raise HTTPException(404, "User not found")
        return user
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))


@app.put("/users/{user_id}")
def update_user(user_id: int, name: str, email: str, db: Session = Depends(get_db)):
    """
    Fully update a user.

    Parameters:
        user_id: ID of the user
        name: Updated name
        email: Updated email

    """
    try:
        user = crud.update_user(db, user_id, {"name": name, "email": email})
        if not user:
            raise HTTPException(404, "User not found")
        return user
    except Exception as e:
        raise HTTPException(500, str(e))


@app.patch("/users/{user_id}")
def patch_user(user_id: int, name: str = None, email: str = None, db: Session = Depends(get_db)):
    """
    Partially update a user.
    
    Parameters:
        user_id: ID of the user
        name: Updated name
        email: Updated email

    """
    try:
        data = {}
        if name:
            data["name"] = name
        if email:
            data["email"] = email

        user = crud.patch_user(db, user_id, data)
        if not user:
            raise HTTPException(404, "User not found")
        return user
    except Exception as e:
        raise HTTPException(500, str(e))


@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    """
    Delete a user by ID.

    Parameters:
        user_id: ID of the user

    """
    try:
        user = crud.delete_user(db, user_id)
        if not user:
            raise HTTPException(404, "User not found")
        return user
    except Exception as e:
        raise HTTPException(500, str(e))

@app.post("/categories")
def create_category(name: str, created_by: int, db: Session = Depends(get_db)):
    """
    Create a new category.

    Parameters:
        name: Category name
        created_by: User ID who created it
    """
    try:
        return crud.create_category(db, {
            "name": name,
            "created_by": created_by
        })
    except Exception as e:
        raise HTTPException(500, str(e))


@app.get("/categories")
def get_categories(db: Session = Depends(get_db)):
    """
    Retrieve all categories from the database.

    """
    try:
        return crud.get_categories(db)
    except Exception as e:
        raise HTTPException(500, str(e))


@app.get("/categories/{category_id}")
def get_category(category_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a specific category by its ID.

    Parameters:
        category_id (int): Unique identifier of the category.

    """
    try:
        category = crud.get_category(db, category_id)
        if not category:
            raise HTTPException(404, "Category not found")
        return category
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))


@app.put("/categories/{category_id}")
def update_category(category_id: int, name: str, db: Session = Depends(get_db)):
    """
    Update an existing category completely.

    Parameters:
        category_id (int): ID of the category to update.
        name (str): New name for the category.

    """
    try:
        category = crud.update_category(db, category_id, {"name": name})
        if not category:
            raise HTTPException(404, "Category not found")
        return category
    except Exception as e:
        raise HTTPException(500, str(e))


@app.patch("/categories/{category_id}")
def patch_category(category_id: int, name: str = None, db: Session = Depends(get_db)):
    """
    Update an existing category partially.

    Parameters:
        category_id (int): ID of the category to update.
        name (str): New name for the category.

    """
    try:
        data = {}
        if name:
            data["name"] = name

        category = crud.patch_category(db, category_id, data)
        if not category:
            raise HTTPException(404, "Category not found")
        return category
    except Exception as e:
        raise HTTPException(500, str(e))


@app.delete("/categories/{category_id}")
def delete_category(category_id: int, db: Session = Depends(get_db)):

    """
    Delete a category by ID.

    Parameters:
        category_id: ID of the user

    """
    try:
        category = crud.delete_category(db, category_id)
        if not category:
            raise HTTPException(404, "Category not found")
        return category
    except Exception as e:
        raise HTTPException(500, str(e))


@app.get("/users/{user_id}/category")
def user_category(user_id: int, db: Session = Depends(get_db)):
    """
    Retrieve all categories created by a specific user.

    Parameters:
        user_id (int): ID of the user whose categories are to be fetched.
    """
    try:
        return db.query(Category).filter(Category.created_by == user_id).all()
    except Exception as e:
        raise HTTPException(500, str(e))


@app.post("/items")
def create_item(
    name: str,
    quantity: int,
    threshold: int,
    price: float,
    supplier: str,
    expiry_date: str,
    category_id: int,
    created_by: int,
    db: Session = Depends(get_db)
):
    """
    Create a new inventory item.

    Parameters:
        name (str): Name of the item.
        quantity (int): Available stock quantity.
        threshold (int): Minimum stock level before considered low.
        price (float): Price per unit.
        supplier (str): Supplier name.
        expiry_date (str): Expiry date of the item (YYYY-MM-DD format).
        category_id (int): ID of the category this item belongs to.
        created_by (int): ID of the user who created the item.
    """
    try:
        return crud.create_item(db, {
            "name": name,
            "quantity": quantity,
            "threshold": threshold,
            "price": price,
            "supplier": supplier,
            "expiry_date": expiry_date,
            "category_id": category_id,
            "created_by": created_by
        })
    except Exception as e:
        raise HTTPException(500, str(e))


@app.get("/items")
def get_items(db: Session = Depends(get_db)):
    """
    Retrieve all items from the inventory.

    """
    try:
        return crud.get_items(db)
    except Exception as e:
        raise HTTPException(500, str(e))


@app.put("/items/{item_id}")
def update_item(
    item_id: int,
    name: str,
    quantity: int,
    threshold: int,
    price: float,
    supplier: str,
    expiry_date: str,
    category_id: int,
    created_by: int,
    db: Session = Depends(get_db)
):
    """
    Fully update an existing item.

    Parameters:
    item_id (int): ID of the item to update.
    name (str): Updated item name.
    quantity (int): Updated stock quantity.
    threshold (int): Updated minimum stock level.
    price (float): Updated price per unit.
    supplier (str): Updated supplier name.
    expiry_date (str): Updated expiry date (YYYY-MM-DD).
    category_id (int): Updated category ID.
    created_by (int): Updated user ID who owns the item.
    db (Session): Database session dependency.

    """
    try:
        item = crud.update_item(db, item_id, {
            "name": name,
            "quantity": quantity,
            "threshold": threshold,
            "price": price,
            "supplier": supplier,
            "expiry_date": expiry_date,
            "category_id": category_id,
            "created_by": created_by
        })

        if not item:
            raise HTTPException(404, "Item not found")

        return item
    except Exception as e:
        raise HTTPException(500, str(e))


@app.patch("/items/{item_id}")
def patch_item(
    item_id: int,
    name: str = None,
    quantity: int = None,
    threshold: int = None,
    price: float = None,
    supplier: str = None,
    expiry_date: str = None,
    category_id: int = None,
    created_by: int = None,
    db: Session = Depends(get_db)
):
    
    """
    Partially update an existing item.

    Parameters:
    item_id (int): ID of the item to update.
    name (str): Updated item name.
    quantity (int): Updated stock quantity.
    threshold (int): Updated minimum stock level.
    price (float): Updated price per unit.
    supplier (str): Updated supplier name.
    expiry_date (str): Updated expiry date (YYYY-MM-DD).
    category_id (int): Updated category ID.
    created_by (int): Updated user ID who owns the item.
    db (Session): Database session dependency.

    """
    try:
        data = {}

        if name:
            data["name"] = name
        if quantity is not None:
            data["quantity"] = quantity
        if threshold is not None:
            data["threshold"] = threshold
        if price is not None:
            data["price"] = price
        if supplier:
            data["supplier"] = supplier
        if expiry_date:
            data["expiry_date"] = expiry_date
        if category_id:
            data["category_id"] = category_id
        if created_by:
            data["created_by"] = created_by

        item = crud.patch_item(db, item_id, data)

        if not item:
            raise HTTPException(404, "Item not found")

        return item
    except Exception as e:
        raise HTTPException(500, str(e))


@app.get("/items/low-stock")
def low_stock(db: Session = Depends(get_db)):
    """
    Retrieve all items that are low in stock.

    """
    try:
        return crud.get_low_stock(db)
    except Exception as e:
        raise HTTPException(500, str(e))


@app.get("/items/expiring-soon")
def expiring_items(db: Session = Depends(get_db)):
    """
    Retrieve items that are expiring within the next 7 days.

    """
    try:
        today = date.today()
        next_week = today + timedelta(days=7)

        return db.query(Item).filter(
            Item.expiry_date >= today,
            Item.expiry_date <= next_week
        ).all()
    except Exception as e:
        raise HTTPException(500, str(e))


@app.get("/items/expired")
def expired_items(db: Session = Depends(get_db)):
    """
    Retrieve all expired items.
    """
    try:
        today = date.today()
        return db.query(Item).filter(
            Item.expiry_date < today
        ).all()
    except Exception as e:
        raise HTTPException(500, str(e))


@app.get("/items/by-supplier")
def items_by_supplier(supplier: str, db: Session = Depends(get_db)):
    """
    Retrieve items filtered by supplier name.

    Parameters:
        supplier (str): Supplier name to filter items.

    """
    try:
        return db.query(Item).filter(
            func.lower(Item.supplier) == supplier.lower()
        ).all()
    except Exception as e:
        raise HTTPException(500, str(e))


@app.get("/users/{user_id}/items")
def user_items(user_id: int, db: Session = Depends(get_db)):
    """
    Retrieve all items created by a specific user.

    Parameters:
        user_id (int): ID of the user.

    """
    try:
        return db.query(Item).filter(Item.created_by == user_id).all()
    except Exception as e:
        raise HTTPException(500, str(e))


@app.get("/categories/{category_id}/items")
def get_items_by_category(category_id: int, db: Session = Depends(get_db)):
    """
    Retrieve all items under a specific category.

    Parameters:
        category_id (int): ID of the category.

    """
    try:
        return db.query(Item).filter(Item.category_id == category_id).all()
    except Exception as e:
        raise HTTPException(500, str(e))


@app.get("/items/{item_id}")
def get_item(item_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a single item by its ID.

    Parameters:
        item_id (int): ID of the item.

    """
    try:
        item = crud.get_item(db, item_id)
        if not item:
            raise HTTPException(404, "Item not found")
        return item
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))


@app.delete("/items/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    """
    Delete an item by its ID.

    Parameters:
        item_id (int): ID of the item to delete.

    """
    try:
        item = crud.delete_item(db, item_id)
        if not item:
            raise HTTPException(404, "Item not found")
        return item
    except Exception as e:
        raise HTTPException(500, str(e))