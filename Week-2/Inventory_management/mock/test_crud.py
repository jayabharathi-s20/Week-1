import pytest
from unittest.mock import MagicMock
from Inventory_management import crud


@pytest.fixture
def mock_db():
    """Mocked DB session."""
    return MagicMock()


# -------------------- USER --------------------

def test_create_user(mock_db):
    """Test user creation with mocked DB."""
    mock_user = MagicMock(id=1, email="john@test.com")

    mock_db.add.return_value = None
    mock_db.commit.return_value = None
    mock_db.refresh.side_effect = lambda x: setattr(x, "id", 1)

    result = crud.create_user(mock_db, {"name": "John", "email": "john@test.com"})

    assert result.email == "john@test.com"
    mock_db.add.assert_called_once()
    mock_db.commit.assert_called_once()


def test_get_user(mock_db):
    """Test fetching user."""
    mock_user = MagicMock(id=1)
    mock_db.query.return_value.filter.return_value.first.return_value = mock_user

    result = crud.get_user(mock_db, 1)

    assert result.id == 1


def test_get_user_not_found(mock_db):
    """Test user not found."""
    mock_db.query.return_value.filter.return_value.first.return_value = None

    result = crud.get_user(mock_db, 999)

    assert result is None


# -------------------- CATEGORY --------------------

def test_create_category(mock_db):
    """Test category creation."""

    # 🔥 IMPORTANT: simulate "no duplicate found"
    mock_db.query.return_value.filter.return_value.first.return_value = None

    mock_db.refresh.side_effect = lambda x: setattr(x, "id", 1)

    result = crud.create_category(mock_db, {"name": "Medicine"})

    assert result is not None
    mock_db.add.assert_called_once()


# -------------------- ITEM --------------------

def test_create_item(mock_db):
    """Test item creation."""
    
    # Mock foreign key checks
    mock_db.query.return_value.filter.return_value.first.side_effect = [
        MagicMock(id=1),  # category exists
        MagicMock(id=1)   # user exists
    ]

    mock_db.refresh.side_effect = lambda x: setattr(x, "id", 1)

    data = {
        "name": "Paracetamol",
        "quantity": 10,
        "threshold": 2,
        "price": 50,
        "supplier": "ABC",
        "expiry_date": "2026-05-10",
        "category_id": 1,
        "created_by": 1
    }

    result = crud.create_item(mock_db, data)

    assert result is not None
    mock_db.add.assert_called_once()


def test_create_item_invalid_category(mock_db):
    """Test invalid category."""
    
    mock_db.query.return_value.filter.return_value.first.side_effect = [
        None  # category does not exist
    ]

    data = {
        "category_id": 999,
        "created_by": 1
    }

    with pytest.raises(ValueError):
        crud.create_item(mock_db, data)


# -------------------- DELETE --------------------

def test_delete_user(mock_db):
    """Test delete user."""
    
    mock_user = MagicMock()
    mock_db.query.return_value.filter.return_value.first.return_value = mock_user

    result = crud.delete_user(mock_db, 1)

    assert result["message"] == "User deleted"
    mock_db.delete.assert_called_once()


def test_delete_user_not_found(mock_db):
    """Test delete non-existing user."""
    
    mock_db.query.return_value.filter.return_value.first.return_value = None

    result = crud.delete_user(mock_db, 999)

    assert result is None