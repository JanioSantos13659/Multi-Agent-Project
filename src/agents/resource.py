import queue

class ResourceAgent:
    def __init__(self, name="ResourceAgent"):
        self.name = name

    def act(self, resource, coord_queue):
        result = f"Resource '{resource}' delivered"
        coord_queue.put(result)
