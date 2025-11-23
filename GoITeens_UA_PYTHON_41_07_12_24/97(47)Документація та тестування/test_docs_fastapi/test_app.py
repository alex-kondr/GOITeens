from fastapi.testclient import TestClient

from main import app


test_client = TestClient(app)
DATA = {
    "new_name": "Крабові палички",
    "count": 10
}


def add_product():
    response = test_client.post("/products/", json=DATA)
    product = response.json()
    print(f"{product = }")
    if "id" not in product:
        raise ValueError()


def get_products():
    response = test_client.post("/products/", json=DATA)
    product = response.json()

    response = test_client.get("/products/")
    products = response.json()

    assert [product] == products


# add_product()
get_products()
