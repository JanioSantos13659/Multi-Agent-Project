import queue
from typing import Any

try:
    from src.helpers.utils import format_output, validate_order
except ModuleNotFoundError:
    from helpers.utils import format_output, validate_order


class CoordinationAgent:
    """Central agent responsible for orchestrating paper sales flow."""

    def __init__(self, inventory_agent=None, quotation_agent=None, sales_agent=None, name="CoordinationAgent", coord_queue=None):
        """Initialize the coordinator with a message queue and updates history."""
        self.name = name
        self.coord_queue = coord_queue or queue.Queue()
        self.updates = []
        self.inventory_agent = inventory_agent
        self.quotation_agent = quotation_agent
        self.sales_agent = sales_agent

    def receive(self, message_or_queue: Any = None) -> None:
        """Receive either a single message or drain messages from a queue."""
        if message_or_queue is None:
            target_queue = self.coord_queue
        elif hasattr(message_or_queue, "empty") and hasattr(message_or_queue, "get"):
            target_queue = message_or_queue
        else:
            self.updates.append(message_or_queue)
            print(f"[Coordination] {message_or_queue}")
            return

        while not target_queue.empty():
            update_message = target_queue.get()
            self.updates.append(update_message)
            print(f"[Coordination] {update_message}")

    def receive_customer_order(self, order: dict[str, Any]) -> dict[str, Any]:
        """Validate and store an incoming customer order."""
        valid_order = validate_order(order)
        self.receive(format_output("Order received", valid_order))
        return valid_order

    def distribute_order(self, order: dict[str, Any]) -> dict[str, Any]:
        """Distribute order handling across inventory, quotation, and sales agents."""
        if not self.inventory_agent or not self.quotation_agent or not self.sales_agent:
            raise ValueError("inventory_agent, quotation_agent and sales_agent are required")

        valid_order = self.receive_customer_order(order)
        reserved = self.inventory_agent.reserve_items(valid_order)

        if not reserved:
            message = format_output("Order status", "out_of_stock")
            self.receive(message)
            return {
                "status": "out_of_stock",
                "order": valid_order,
            }

        proposal = self.quotation_agent.generate_proposal(valid_order)
        self.receive(format_output("Proposal generated", proposal))

        confirmed = self.sales_agent.confirm_order(reserved)
        if not confirmed:
            message = format_output("Order status", "not_confirmed")
            self.receive(message)
            return {
                "status": "not_confirmed",
                "order": valid_order,
                "proposal": proposal,
            }

        transaction = self.sales_agent.register_transaction(proposal)
        self.receive(format_output("Sale finalized", transaction))

        return {
            "status": "completed",
            "order": valid_order,
            "proposal": proposal,
            "transaction": transaction,
        }

    def respond_user(self) -> None:
        """Print aggregated updates as the final user response."""
        print(f"Final response to user ({len(self.updates)} update(s)):")
        for update_message in self.updates:
            print(" -", update_message)
