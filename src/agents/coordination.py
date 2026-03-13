import queue
from typing import Any


class CoordinationAgent:
    """Central agent responsible for orchestrating message flow."""

    def __init__(self, name="CoordinationAgent", coord_queue=None):
        """Initialize the coordinator with a message queue and updates history."""
        self.name = name
        self.coord_queue = coord_queue or queue.Queue()
        self.updates = []

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

    def distribute(self, requests: list[dict[str, str]], task_agent, resource_agent) -> None:
        """Route requests to specialized agents and collect their responses."""
        total_requests = len(requests)
        print(f"[Coordination] Starting distribution of {total_requests} request(s)")

        for index, request in enumerate(requests, start=1):
            request_type = request.get("type")
            payload = request.get("payload")
            print(f"[Coordination] Routing request {index}/{total_requests}: type={request_type}")

            if request_type == "task":
                task_agent.act(payload, self.coord_queue)
            elif request_type == "resource":
                resource_agent.act(payload, self.coord_queue)
            else:
                self.receive(f"Unsupported request type: {request_type}")

        # Drain all produced messages after routing completes.
        self.receive(self.coord_queue)

    def respond_user(self) -> None:
        """Print aggregated updates as the final user response."""
        print(f"Final response to user ({len(self.updates)} update(s)):")
        for update_message in self.updates:
            print(" -", update_message)
