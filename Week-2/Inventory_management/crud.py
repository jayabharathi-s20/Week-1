from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import date, timedelta
from models import User, Category, Item

def create_user(db: Session, data: dict):
    """
    Create a new user.

    Args:
        db: Database session
        data: Dictionary containing user details (name, email)

    Returns:
        Created user object
    """
    user = User(**data)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_users(db: Session):
    """
    Retrieve all users.

    Args:
        db: Database session

    Returns:
        List of users
    """
    return db.query(User).all()


def get_user(db: Session, user_id: int):
    """
    Get a single user by ID.

    Args:
        db: Database session
        user_id: ID of the user

    Returns:
        User object or None
    """
    return db.query(User).filter(User.id == user_id).first()


def update_user(db: Session, user_id: int, data: dict):
    """
    Update all fields of a user.

    Args:
        db: Database session
        user_id: User ID
        data: Updated data

    Returns:
        Updated user or None
    """
    user = get_user(db, user_id)
    if not user:
        return None

    for key, value in data.items():
        setattr(user, key, value)

    db.commit()
    db.refresh(user)
    return user


def patch_user(db: Session, user_id: int, data: dict):
    """
    Partially update user fields.

    Args:
        db: Database session
        user_id: User ID
        data: Partial fields to update

    Returns:
        Updated user or None
    """
    user = get_user(db, user_id)
    if not user:
        return None

    for key, value in data.items():
        if value is not None:
            setattr(user, key, value)

    db.commit()
    db.refresh(user)
    return user


def delete_user(db: Session, user_id: int):
    """
    Delete a user by ID.

    Args:
        db: Database session
        user_id: User ID

    Returns:
        Success message or None
    """
    user = get_user(db, user_id)
    if not user:
        return None

    db.delete(user)
    db.commit()
    return {"message": "User deleted"}

def create_category(db: Session, data: dict):
    """
    Create a new category.

    Args:
        db: Database session
        data: Category data (name, created_by)

    Returns:
        Created category
    """
    category = Category(**data)
    db.add(category)
    db.commit()
    db.refresh(category)
    return category


def get_categories(db: Session):
    """
    Get all categories.

    Returns:
        List of categories
    """
    return db.query(Category).all()


def get_category(db: Session, category_id: int):
    """
    Get category by ID.

    Returns:
        Category or None
    """
    return db.query(Category).filter(Category.id == category_id).first()


def update_category(db: Session, category_id: int, data: dict):
    """
    Fully update a category.

    Returns:
        Updated category or None
    """
    category = get_category(db, category_id)
    if not category:
        return None

    for key, value in data.items():
        setattr(category, key, value)

    db.commit()
    db.refresh(category)
    return category


def patch_category(db: Session, category_id: int, data: dict):
    """
    Partially update a category.

    Returns:
        Updated category or None
    """
    category = get_category(db, category_id)
    if not category:
        return None

    for key, value in data.items():
        if value is not None:
            setattr(category, key, value)

    db.commit()
    db.refresh(category)
    return category


def delete_category(db: Session, category_id: int):
    """
    Delete a category.

    Returns:
        Success message or None
    """
    category = get_category(db, category_id)
    if not category:
        return None

    db.delete(category)
    db.commit()
    return {"message": "Category deleted"}


def get_categories_by_user(db: Session, user_id: int):
    """
    Get all categories created by a user.

    Args:
        user_id: User ID

    Returns:
        List of categories
    """
    return db.query(Category).filter(Category.created_by == user_id).all()


def create_item(db: Session, data: dict):
    """
    Create a new item.

    Returns:
        Created item
    """
    item = Item(**data)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def get_items(db: Session):
    """
    Get all items.

    Returns:
        List of items
    """
    return db.query(Item).all()


def get_item(db: Session, item_id: int):
    """
    Get item by ID.

    Returns:
        Item or None
    """
    return db.query(Item).filter(Item.id == item_id).first()


def update_item(db: Session, item_id: int, data: dict):
    """
    Fully update an item.

    Returns:
        Updated item or None
    """
    item = get_item(db, item_id)
    if not item:
        return None

    for key, value in data.items():
        setattr(item, key, value)

    db.commit()
    db.refresh(item)
    return item


def patch_item(db: Session, item_id: int, data: dict):
    """
    Partially update an item.

    Returns:
        Updated item or None
    """
    item = get_item(db, item_id)
    if not item:
        return None

    for key, value in data.items():
        if value is not None:
            setattr(item, key, value)

    db.commit()
    db.refresh(item)
    return item


def delete_item(db: Session, item_id: int):
    """
    Delete an item.

    Returns:
        Success message or None
    """
    item = get_item(db, item_id)
    if not item:
        return None

    db.delete(item)
    db.commit()
    return {"message": "Item deleted"}


def get_user_items(db: Session, user_id: int):
    """
    Get all items created by a user.

    Returns:
        List of items
    """
    return db.query(Item).filter(Item.created_by == user_id).all()


def get_items_by_category(db: Session, category_id: int):
    """
    Get all items under a category.

    Returns:
        List of items
    """
    return db.query(Item).filter(Item.category_id == category_id).all()


def get_low_stock(db: Session):
    """
    Get items where quantity is below or equal to threshold.

    Returns:
        List of low-stock items
    """
    return db.query(Item).filter(Item.quantity <= Item.threshold).all()


def get_expiring_items(db: Session):
    """
    Get items expiring within the next 7 days.

    Returns:
        List of items
    """
    today = date.today()
    next_week = today + timedelta(days=7)

    return db.query(Item).filter(
        Item.expiry_date >= today,
        Item.expiry_date <= next_week
    ).all()


def get_expired_items(db: Session):
    """
    Get already expired items.

    Returns:
        List of expired items
    """
    today = date.today()
    return db.query(Item).filter(Item.expiry_date < today).all()


def get_items_by_supplier(db: Session, supplier: str):
    """
    Get items filtered by supplier name (case-insensitive).

    Returns:
        List of items
    """
    return db.query(Item).filter(
        func.lower(Item.supplier) == supplier.lower()
    ).all()