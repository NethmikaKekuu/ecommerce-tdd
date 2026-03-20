import pytest
from src.checkout import Checkout


class FakePaymentSuccess:
    def charge(self, amount, token):
        return True


class FakePaymentFail:
    def charge(self, amount, token):
        return False


class FakeInventory:
    def getAvailable(self, sku):
        return 10


class FakeCatalog:
    def get(self, sku):
        return type("Product", (), {"sku": sku, "price": 100})


class FakeCart:
    def __init__(self):
        self.items = {"SKU1": type("Item", (), {"quantity": 2})}

    def total(self):
        return 200


class FakeDiscount:
    def apply(self, items):
        return 180  # simulate discount applied


def test_checkout_success():
    checkout = Checkout(
        cart=FakeCart(),
        payment=FakePaymentSuccess(),
        discount_engine=FakeDiscount(),
        inventory=FakeInventory()
    )

    result = checkout.process("token")

    assert result is True


def test_checkout_payment_failure():
    checkout = Checkout(
        cart=FakeCart(),
        payment=FakePaymentFail(),
        discount_engine=FakeDiscount(),
        inventory=FakeInventory()
    )

    with pytest.raises(ValueError):
        checkout.process("token")