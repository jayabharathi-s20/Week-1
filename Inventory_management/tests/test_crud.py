import pytest
from datetime import date, timedelta
from app import crud


@pytest.fixture
def user_data():
    """Provide valid user data."""
    return {"name": "John", "email": "john@test.com"}


@pytest.fixture
def category_data():
    """Provide valid category data."""
    return {"name": "Medicine"}


@pytest.fixture
def item_base_data():
    """Provide base item data."""
    return {
        "name": "Paracetamol",
        "quantity": 10,
        "threshold": 2,
        "price": 50.0,
        "supplier": "ABC",
        "expiry_date": date.today() + timedelta(days=5),
    }


@pytest.fixture
def user(db, user_data):
    """Create a user in database."""
    return crud.create_user(db, user_data)


@pytest.fixture
def category(db, category_data):
    """Create a category in database."""
    return crud.create_category(db, category_data)


@pytest.fixture
def item(db, user, category, item_base_data):
    """Create an item with valid foreign keys."""
    data = item_base_data.copy()
    data.update({
        "category_id": category.id,
        "created_by": user.id
    })
    return crud.create_item(db, data)


def test_create_user(db, user_data):
    """Validate user creation."""
    user = crud.create_user(db, user_data)
    assert user.id is not None
    assert user.email == user_data["email"]


def test_create_user_duplicate(db):
    """Ensure duplicate email raises ValueError."""
    crud.create_user(db, {"name": "A", "email": "dup@test.com"})
    try:
        crud.create_user(db, {"name": "B", "email": "dup@test.com"})
        assert False
    except ValueError:
        assert True


def test_get_user(db, user):
    """Validate retrieving existing user."""
    fetched = crud.get_user(db, user.id)
    assert fetched.id == user.id


def test_get_user_not_found(db):
    """Validate retrieving non-existing user returns None."""
    result = crud.get_user(db, 999)
    assert result is None


def test_get_users(db, user):
    """Validate retrieving all users."""
    users = crud.get_users(db)
    assert len(users) >= 1


def test_update_user_not_found(db):
    """Ensure updating non-existing user returns None."""
    try:
        result = crud.update_user(db, 999, {"name": "X"})
        assert result is None
    except Exception:
        assert False


def test_patch_user(db, user):
    """Validate partial update of user."""
    updated = crud.patch_user(db, user.id, {"name": "Patch"})
    assert updated.name == "Patch"


def test_delete_user(db, user):
    """Validate deleting user."""
    res = crud.delete_user(db, user.id)
    assert res["message"] == "User deleted"


def test_delete_user_not_found(db):
    """Ensure deleting non-existing user returns None."""
    result = crud.delete_user(db, 999)
    assert result is None


def test_create_category(db, category_data):
    """Validate category creation."""
    category = crud.create_category(db, category_data)
    assert category.id is not None


def test_duplicate_category(db, category_data):
    """Ensure duplicate category raises ValueError."""
    crud.create_category(db, category_data)
    try:
        crud.create_category(db, category_data)
        assert False
    except ValueError:
        assert True


def test_get_category(db, category):
    """Validate retrieving category."""
    fetched = crud.get_category(db, category.id)
    assert fetched.id == category.id


def test_get_categories(db, category):
    """Validate retrieving all categories."""
    categories = crud.get_categories(db)
    assert len(categories) >= 1



def test_patch_category(db, category):
    """Validate partial update of category."""
    updated = crud.patch_category(db, category.id, {"name": "Patch"})
    assert updated.name == "Patch"


def test_delete_category(db, category):
    """Validate deleting category."""
    res = crud.delete_category(db, category.id)
    assert res["message"] == "Category deleted"


def test_delete_category_not_found(db):
    """Ensure deleting non-existing category returns None."""
    result = crud.delete_category(db, 999)
    assert result is None


def test_create_item(db, user, category, item_base_data):
    """Validate item creation."""
    data = item_base_data.copy()
    data.update({
        "category_id": category.id,
        "created_by": user.id
    })
    item = crud.create_item(db, data)
    assert item.id is not None


def test_create_item_invalid_category(db, user, item_base_data):
    """Ensure invalid category raises ValueError."""
    data = item_base_data.copy()
    data.update({
        "category_id": 999,
        "created_by": user.id
    })
    try:
        crud.create_item(db, data)
        assert False
    except ValueError:
        assert True


def test_create_item_invalid_user(db, category, item_base_data):
    """Ensure invalid user raises ValueError."""
    data = item_base_data.copy()
    data.update({
        "category_id": category.id,
        "created_by": 999
    })
    try:
        crud.create_item(db, data)
        assert False
    except ValueError:
        assert True


def test_get_item(db, item):
    """Validate retrieving item."""
    fetched = crud.get_item(db, item.id)
    assert fetched.id == item.id


def test_get_items(db, item):
    """Validate retrieving all items."""
    items = crud.get_items(db)
    assert len(items) >= 1



def test_patch_item(db, item):
    """Validate partial update of item."""
    updated = crud.patch_item(db, item.id, {"name": "Patch"})
    assert updated.name == "Patch"


def test_delete_item(db, item):
    """Validate deleting item."""
    res = crud.delete_item(db, item.id)
    assert res["message"] == "Item deleted"


def test_delete_item_not_found(db):
    """Ensure deleting non-existing item returns None."""
    result = crud.delete_item(db, 999)
    assert result is None


def test_low_stock(db, user, category, item_base_data):
    """Validate low stock filter."""
    data = item_base_data.copy()
    data.update({
        "quantity": 1,
        "threshold": 5,
        "category_id": category.id,
        "created_by": user.id
    })
    crud.create_item(db, data)
    items = crud.get_low_stock(db)
    assert len(items) == 1


def test_expiring_items(db, user, category, item_base_data):
    """Validate expiring items filter."""
    data = item_base_data.copy()
    data.update({
        "expiry_date": date.today() + timedelta(days=3),
        "category_id": category.id,
        "created_by": user.id
    })
    crud.create_item(db, data)
    items = crud.get_expiring_items(db)
    assert len(items) == 1


def test_get_items_by_supplier(db, item):
    """Validate supplier filter."""
    items = crud.get_items_by_supplier(db, "ABC")
    assert len(items) >= 1


def test_get_user_items(db, user, item):
    """Validate user-specific items."""
    items = crud.get_user_items(db, user.id)
    assert len(items) >= 1


def test_get_items_by_category(db, category, item):
    """Validate category filter."""
    items = crud.get_items_by_category(db, category.id)
    assert len(items) >= 1