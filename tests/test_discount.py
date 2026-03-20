import pytest
from src.discount import DiscountEngine


def test_bulk_discount():
    engine = DiscountEngine()

    # sku: (price, quantity)
    items = {
        "SKU1": (100, 10)  # qualifies for bulk discount
    }

    total = engine.apply(items)

    # 10 * 100 = 1000 → 10% off → 900
    assert total == 900


def test_order_discount():
    engine = DiscountEngine()

    items = {
        "SKU1": (200, 5)  # total = 1000
    }

    total = engine.apply(items)

    # order >= 1000 → 5% off → 950
    assert total == 950


def test_combined_discounts():
    engine = DiscountEngine()

    items = {
        "SKU1": (100, 10),  # bulk → 900
        "SKU2": (100, 1)    # +100 → 1000 total → order discount
    }

    total = engine.apply(items)

    # subtotal = 1000 → 5% off → 950
    assert total == 950