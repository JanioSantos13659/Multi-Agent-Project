try:
    from src.helpers.utils import calculate_discount, validate_order
except ModuleNotFoundError:
    from helpers.utils import calculate_discount, validate_order


class QuotationAgent:
    """Agent responsible for pricing and quotation proposals."""

    def __init__(self, price_table=None, name="QuotationAgent"):
        self.name = name
        self.price_table = price_table or {"A4": 0.12, "Carta": 0.10}

    def calculate_price(self, quantity: int, paper_type: str) -> float:
        unit_price = self.price_table.get(paper_type)
        if unit_price is None:
            raise ValueError(f"unknown paper type: {paper_type}")
        return round(unit_price * quantity, 2)

    def apply_discounts(self, total_value: float, quantity: int) -> float:
        discount_rate = calculate_discount(quantity)
        return round(total_value * (1 - discount_rate), 2)

    def generate_proposal(self, order):
        validated_order = validate_order(order)
        quantity = validated_order["quantity"]
        paper_type = validated_order["paper_type"]

        subtotal = self.calculate_price(quantity, paper_type)
        discount_rate = calculate_discount(quantity)
        total = self.apply_discounts(subtotal, quantity)

        return {
            "client": validated_order["client"],
            "paper_type": paper_type,
            "quantity": quantity,
            "subtotal": subtotal,
            "discount_rate": discount_rate,
            "total": total,
        }
