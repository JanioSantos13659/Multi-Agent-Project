from queue import Queue

try:
    from src.utils import validate_input
except ModuleNotFoundError:
    from utils import validate_input


class TaskAgent:
    """Agent responsible for handling and validating task operations."""

    def __init__(self, name="TaskAgent"):
        """Create a task agent with a display name."""
        self.name = name

    def process(self, task: str) -> str:
        """Process a single task and return a standardized completion message."""
        valid_task = validate_input(task, "task")
        return f"Task '{valid_task}' completed"

    def act(self, task: str, coord_queue: Queue) -> str:
        """Process a task and publish the result to the coordination queue."""
        result = self.process(task)
        coord_queue.put(result)
        return result

