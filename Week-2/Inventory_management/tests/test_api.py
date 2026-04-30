from datetime import date, timedelta


def test_create_user_api(client):
    res = client.post("/users", json={
        "name": "John",
        "email": "john@test.com"
    })

    assert res.status_code == 200
    assert res.json()["email"] == "john@test.com"


def test_duplicate_user_api(client):
    client.post("/users", json={
        "name": "John",
        "email": "dup@test.com"
    })

    res = client.post("/users", json={
        "name": "John2",
        "email": "dup@test.com"
    })

    assert res.status_code == 400


def test_get_users_api(client):
    res = client.get("/users")
    assert res.status_code == 200


def test_create_category_api(client):
    res = client.post("/categories", json={"name": "Medicine"})
    assert res.status_code == 200


def test_create_item_api(client):
    user = client.post("/users", json={
        "name": "John",
        "email": "item@test.com"
    }).json()

    category = client.post("/categories", json={
        "name": "Food"
    }).json()

    res = client.post("/items", json={
        "name": "Rice",
        "quantity": 10,
        "threshold": 2,
        "price": 50,
        "supplier": "ABC",
        "expiry_date": str(date.today() + timedelta(days=5)),
        "category_id": category["id"],
        "created_by": user["id"]
    })

    assert res.status_code == 200


def test_low_stock_api(client):
    res = client.get("/items/low-stock")
    assert res.status_code == 200


def test_expiring_items_api(client):
    res = client.get("/items/expiring-soon")
    assert res.status_code == 200