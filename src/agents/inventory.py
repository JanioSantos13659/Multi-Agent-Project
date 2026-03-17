try:
    from src.helpers.utils import validate_order
except ModuleNotFoundError:
    from helpers.utils import validate_order


class InventoryAgent:
    """Agent responsible for managing paper inventory."""

    def __init__(self, initial_stock=None, name="InventoryAgent"):
        self.name = name
        self.stock = initial_stock or {"A4": 1000, "Carta": 800}

    def check_availability(self, paper_type: str, quantity: int) -> bool:
        available = self.stock.get(paper_type, 0)
        return available >= quantity

    def update_quantity(self, paper_type: str, quantity_change: int) -> int:
        current_quantity = self.stock.get(paper_type, 0)
        new_quantity = current_quantity + quantity_change
        if new_quantity < 0:
            raise ValueError("stock cannot be negative")
        self.stock[paper_type] = new_quantity
        return new_quantity

    def reserve_items(self, order):
        validated_order = validate_order(order)
        paper_type = validated_order["paper_type"]
        quantity = validated_order["quantity"]

        if not self.check_availability(paper_type, quantity):
            return False

        self.update_quantity(paper_type, -quantity)
        return True
