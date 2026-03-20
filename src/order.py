from datetime import datetime

class Order:
    def __init__(self, items, total):
        self.items = items
        self.total = total
        self.timestamp = datetime.now()

    def to_dict(self):
        return {
            "items": {sku: item.quantity for sku, item in self.items.items()},
            "total": self.total,
            "timestamp": self.timestamp.isoformat()
        }

class OrderRepository:
    def save(self, order):
        raise NotImplementedError
    