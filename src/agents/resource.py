from queue import Queue

try:
    from src.utils import format_message
except ModuleNotFoundError:
    from utils import format_message


class ResourceAgent:
    """Agent responsible for handling resource provisioning messages."""

    def __init__(self, name="ResourceAgent"):
        """Create a resource agent with a display name."""
        self.name = name

    def provide(self, resource: str) -> str:
        """Return a standardized message indicating resource delivery."""
        return format_message("Resource", resource, "delivered")

    def act(self, resource: str, coord_queue: Queue) -> str:
        """Provide a resource and publish the result to the coordination queue."""
        result = self.provide(resource)
        coord_queue.put(result)
        return result
