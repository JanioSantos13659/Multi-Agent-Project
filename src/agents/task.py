import queue

class TaskAgent:
    def __init__(self, name="TaskAgent"):
        self.name = name

    def act(self, task, coord_queue):
        result = f"Task '{task}' completed"
        coord_queue.put(result)

