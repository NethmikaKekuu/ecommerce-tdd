from src.catalog import Catalog
from src.product import Product

def test_add_and_get_product():
    c = Catalog()
    p = Product("SKU1", "Laptop", 1000)

    c.add(p)
    assert c.get("SKU1") == p

def test_missing_product():
    c = Catalog()
    assert c.get("XYZ") is None