class LineItem:
    def __init__(self, sku, price, quantity):
        if quantity <= 0:
            raise ValueError("Invalid quantity")

        self.sku = sku
        self.price = price
        self.quantity = quantity

    def total(self):
        return self.price * self.quantity


class Cart:
    def __init__(self, catalog):
        self.catalog = catalog
        self.items = {}

    def add(self, sku, quantity):
        product = self.catalog.get(sku)
        if not product:
            raise ValueError("Product not found")

        if sku in self.items:
            self.items[sku].quantity += quantity
        else:
            self.items[sku] = LineItem(sku, product.price, quantity)

    def remove(self, sku):
        self.items.pop(sku, None)

    def total(self):
        return sum(item.total() for item in self.items.values())