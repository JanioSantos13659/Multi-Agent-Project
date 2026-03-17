class SalesAgent:
    """Agent responsible for closing sales and tracking transaction status."""

    def __init__(self, name="SalesAgent"):
        self.name = name
        self.transactions = []

    def confirm_order(self, inventory_reserved: bool) -> bool:
        return inventory_reserved

    def register_transaction(self, proposal: dict) -> dict:
        transaction = {
            "sale_id": len(self.transactions) + 1,
            "client": proposal["client"],
            "paper_type": proposal["paper_type"],
            "quantity": proposal["quantity"],
            "total": proposal["total"],
            "status": "confirmed",
        }
        self.transactions.append(transaction)
        return transaction

    def update_sale_status(self, sale_id: int, status: str) -> dict:
        for transaction in self.transactions:
            if transaction["sale_id"] == sale_id:
                transaction["status"] = status
                return transaction

        raise ValueError(f"sale_id not found: {sale_id}")
