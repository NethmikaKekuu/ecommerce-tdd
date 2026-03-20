import pytest
from src.checkout import Checkout


class FakePayment:
    def charge(self, amount, token):
        return True


class FakeInventory:
    def getAvailable(self, sku):
        return 10


class FakeDiscount:
    def apply(self, items):
        return 200


class FakeCart:
    def __init__(self):
        self.items = {"SKU1": type("Item", (), {"quantity": 2})}

    def total(self):
        return 200


class FakeOrderRepo:
    def __init__(self):
        self.saved_order = None

    def save(self, order):
        self.saved_order = order


def test_order_created_on_successful_checkout():
    repo = FakeOrderRepo()

    checkout = Checkout(
        cart=FakeCart(),
        payment=FakePayment(),
        discount_engine=FakeDiscount(),
        inventory=FakeInventory(),
        order_repo=repo
    )

    result = checkout.process("token")

    assert result is True
    assert repo.saved_order is not None