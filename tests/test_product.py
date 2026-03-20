import pytest
from src.product import Product

def test_create_product_success():
    p = Product("SKU1", "Laptop", 1000)
    assert p.sku == "SKU1"

def test_negative_price():
    with pytest.raises(ValueError):
        Product("SKU2", "Phone", -10)