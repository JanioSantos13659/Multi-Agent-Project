import queue
from src.utils import validate_input

class TaskAgent:
    def __init__(self, name="TaskAgent"):
        self.name = name

    def process(self, task):
        valid_task = validate_input(task, "task")
        return f"Task '{valid_task}' completed"

    def act(self, task, coord_queue):
        result = self.process(task)
        coord_queue.put(result)
        return result

