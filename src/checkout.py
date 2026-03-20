class Checkout:
    def __init__(self, cart, payment, discount_engine, inventory, order_repo=None):
        self.cart = cart
        self.payment = payment
        self.discount_engine = discount_engine
        self.inventory = inventory
        self.order_repo = order_repo

    def _validate_inventory(self):
        for sku, item in self.cart.items.items():
            available = self.inventory.getAvailable(sku)
            if item.quantity > available:
                raise ValueError("Insufficient inventory")

    def _calculate_total(self):
        items = {
            sku: (100, item.quantity)
            for sku, item in self.cart.items.items()
        }
        return self.discount_engine.apply(items)

    def process(self, token):
        self._validate_inventory()

        total = self._calculate_total()

        if not self.payment.charge(total, token):
            raise ValueError("Payment failed")

        # ✅ NEW: create and save order
        if self.order_repo:
            from src.order import Order
            order = Order(self.cart.items, total)
            self.order_repo.save(order)

        return True