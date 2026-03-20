import pytest
from src.cart import Cart

# Fake catalog to isolate Cart behavior
class FakeCatalog:
    def __init__(self):
        self.products = {
            "SKU1": type("Product", (), {"sku": "SKU1", "price": 100}),
            "SKU2": type("Product", (), {"sku": "SKU2", "price": 200}),
        }

    def get(self, sku):
        return self.products.get(sku)


def test_add_item_success():
    cart = Cart(FakeCatalog())

    cart.add("SKU1", 2)

    assert cart.items["SKU1"].quantity == 2


def test_add_invalid_product():
    cart = Cart(FakeCatalog())

    with pytest.raises(ValueError):
        cart.add("INVALID", 1)


def test_add_invalid_quantity():
    cart = Cart(FakeCatalog())

    with pytest.raises(ValueError):
        cart.add("SKU1", 0)


def test_remove_item():
    cart = Cart(FakeCatalog())

    cart.add("SKU1", 2)
    cart.remove("SKU1")

    assert "SKU1" not in cart.items


def test_total_calculation():
    cart = Cart(FakeCatalog())

    cart.add("SKU1", 2)  # 2 * 100 = 200
    cart.add("SKU2", 1)  # 1 * 200 = 200

    assert cart.total() == 400