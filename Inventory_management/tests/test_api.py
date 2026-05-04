import pytest
from datetime import date, timedelta



@pytest.mark.parametrize("payload, expected_status", [
    ({"name": "John", "email": "john@test.com"}, 200),
    ({"name": "", "email": "john@test.com"}, 422),
    ({"name": "A", "email": "bademail"}, 422),
])
def test_create_user_api(client, payload, expected_status):
    """Validate user creation API."""
    try:
        res = client.post("/users", json=payload)
        assert res.status_code == expected_status

        if expected_status == 200:
            assert res.json()["email"] == payload["email"]
    except Exception as e:
        assert False, str(e)


@pytest.mark.parametrize("endpoint, expected_status", [
    ("/users", 200),
    ("/categories", 200),
    ("/items", 200),
    ("/items/low-stock", 200),
    ("/items/expiring-soon", 200),
])
def test_get_endpoints_api(client, endpoint, expected_status):
    """Validate multiple GET endpoints."""
    try:
        res = client.get(endpoint)
        assert res.status_code == expected_status
    except Exception as e:
        assert False, str(e)


def test_get_user_by_id_api(client):
    """Validate fetching user by ID."""
    try:
        user = client.post("/users", json={
            "name": "Test",
            "email": "get@test.com"
        }).json()

        res = client.get(f"/users/{user['id']}")
        assert res.status_code == 200
    except Exception as e:
        assert False, str(e)


@pytest.mark.parametrize("user_id, expected_status", [
    (999, 404),
    (1000, 404),
    (-1, 404),
])
def test_get_user_not_found_api(client, user_id, expected_status):
    """Validate user not found case."""
    try:
        res = client.get(f"/users/{user_id}")
        assert res.status_code == expected_status
    except Exception as e:
        assert False, str(e)


def test_update_user_api(client):
    """Validate updating user."""
    try:
        user = client.post("/users", json={
            "name": "Old",
            "email": "old@test.com"
        }).json()

        res = client.put(f"/users/{user['id']}", json={
            "name": "New",
            "email": "new@test.com"
        })

        assert res.status_code == 200
        assert res.json()["name"] == "New"
    except Exception as e:
        assert False, str(e)


def test_patch_user_api(client):
    """Validate partial update of user."""
    try:
        user = client.post("/users", json={
            "name": "Patch",
            "email": "patch@test.com"
        }).json()

        res = client.patch(f"/users/{user['id']}", json={"name": "Updated"})
        assert res.status_code == 200
        assert res.json()["name"] == "Updated"
    except Exception as e:
        assert False, str(e)


def test_delete_user_api(client):
    """Validate deleting user."""
    try:
        user = client.post("/users", json={
            "name": "Delete",
            "email": "delete@test.com"
        }).json()

        res = client.delete(f"/users/{user['id']}")
        assert res.status_code == 200
    except Exception as e:
        assert False, str(e)



@pytest.mark.parametrize("category_name, expected_status", [
    ("Medicine", 200),
    ("Food", 200),
    ("", 422),
])
def test_create_category_api(client, category_name, expected_status):
    """Validate category creation."""
    try:
        res = client.post("/categories", json={"name": category_name})
        assert res.status_code in [expected_status, 400]
    except Exception as e:
        assert False, str(e)


def test_duplicate_category_api(client):
    """Validate duplicate category handling."""
    try:
        client.post("/categories", json={"name": "Food"})
        res = client.post("/categories", json={"name": "Food"})
        assert res.status_code == 400
    except Exception as e:
        assert False, str(e)


def test_get_category_by_id_api(client):
    """Validate fetching category by ID."""
    try:
        category = client.post("/categories", json={"name": "TestCat"}).json()
        res = client.get(f"/categories/{category['id']}")
        assert res.status_code == 200
    except Exception as e:
        assert False, str(e)


def test_delete_category_api(client):
    """Validate deleting category."""
    try:
        category = client.post("/categories", json={"name": "DeleteCat"}).json()
        res = client.delete(f"/categories/{category['id']}")
        assert res.status_code == 200
    except Exception as e:
        assert False, str(e)



def create_user_and_category(client):
    """Helper to create user and category."""
    user = client.post("/users", json={
        "name": "ItemUser",
        "email": "itemuser@test.com"
    }).json()

    category = client.post("/categories", json={
        "name": "ItemCat"
    }).json()

    return user, category



@pytest.mark.parametrize("quantity, price, expected_status", [
    (10, 50, 200),
    (-1, 50, 422),
    (5, -10, 422),
])
def test_create_item_api(client, quantity, price, expected_status):
    """Validate item creation."""
    try:
        user, category = create_user_and_category(client)

        res = client.post("/items", json={
            "name": "Rice",
            "quantity": quantity,
            "threshold": 2,
            "price": price,
            "supplier": "ABC",
            "expiry_date": str(date.today() + timedelta(days=5)),
            "category_id": category["id"],
            "created_by": user["id"]
        })

        assert res.status_code == expected_status
    except Exception as e:
        assert False, str(e)


def test_get_item_by_id_api(client):
    """Validate fetching item by ID."""
    try:
        user, category = create_user_and_category(client)

        item = client.post("/items", json={
            "name": "Milk",
            "quantity": 5,
            "threshold": 2,
            "price": 30,
            "supplier": "ABC",
            "expiry_date": str(date.today() + timedelta(days=5)),
            "category_id": category["id"],
            "created_by": user["id"]
        }).json()

        res = client.get(f"/items/{item['id']}")
        assert res.status_code == 200
    except Exception as e:
        assert False, str(e)


def test_update_item_api(client):
    """Validate updating item."""
    try:
        user, category = create_user_and_category(client)

        item = client.post("/items", json={
            "name": "Old",
            "quantity": 5,
            "threshold": 2,
            "price": 30,
            "supplier": "ABC",
            "expiry_date": str(date.today() + timedelta(days=5)),
            "category_id": category["id"],
            "created_by": user["id"]
        }).json()

        res = client.put(f"/items/{item['id']}", json={
            "name": "New",
            "quantity": 10,
            "threshold": 3,
            "price": 60,
            "supplier": "XYZ",
            "expiry_date": str(date.today() + timedelta(days=10)),
            "category_id": category["id"],
            "created_by": user["id"]
        })

        assert res.status_code == 200
    except Exception as e:
        assert False, str(e)


def test_delete_item_api(client):
    """Validate deleting item."""
    try:
        user, category = create_user_and_category(client)

        item = client.post("/items", json={
            "name": "Delete",
            "quantity": 5,
            "threshold": 2,
            "price": 30,
            "supplier": "ABC",
            "expiry_date": str(date.today() + timedelta(days=5)),
            "category_id": category["id"],
            "created_by": user["id"]
        }).json()

        res = client.delete(f"/items/{item['id']}")
        assert res.status_code == 200
    except Exception as e:
        assert False, str(e)



@pytest.mark.parametrize("supplier, expected_status", [
    ("ABC", 200),
    ("XYZ", 200),
    ("UNKNOWN", 200),
])
def test_items_by_supplier_api(client, supplier, expected_status):
    """Validate supplier filter."""
    try:
        res = client.get(f"/items/by-supplier?supplier={supplier}")
        assert res.status_code == expected_status
    except Exception as e:
        assert False, str(e)


def test_user_items_api(client):
    """Validate user items endpoint."""
    try:
        user = client.post("/users", json={
            "name": "UserItems",
            "email": "ui@test.com"
        }).json()

        res = client.get(f"/users/{user['id']}/items")
        assert res.status_code == 200
    except Exception as e:
        assert False, str(e)


def test_items_by_category_api(client):
    """Validate category items endpoint."""
    try:
        category = client.post("/categories", json={"name": "CatItems"}).json()

        res = client.get(f"/categories/{category['id']}/items")
        assert res.status_code == 200
    except Exception as e:
        assert False, str(e)