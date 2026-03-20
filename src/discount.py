class DiscountRule:
    def apply(self, items, current_total):
        raise NotImplementedError


class BulkDiscountRule(DiscountRule):
    def apply(self, items, current_total):
        total = 0
        for sku, (price, qty) in items.items():
            line_total = price * qty
            if qty >= 10:
                line_total *= 0.9
            total += line_total
        return total


class OrderDiscountRule(DiscountRule):
    def apply(self, items, current_total):
        if current_total >= 1000:
            return current_total * 0.95
        return current_total


class DiscountEngine:
    def __init__(self, rules=None):
        self.rules = rules or [
            BulkDiscountRule(),
            OrderDiscountRule()
        ]

    def apply(self, items):
        total = 0

        # First rule calculates subtotal
        total = self.rules[0].apply(items, total)

        # Apply remaining rules
        for rule in self.rules[1:]:
            total = rule.apply(items, total)

        return total