import queue
from src.utils import format_message

class ResourceAgent:
    def __init__(self, name="ResourceAgent"):
        self.name = name

    def provide(self, resource):
        return format_message("Resource", resource, "delivered")

    def act(self, resource, coord_queue):
        result = self.provide(resource)
        coord_queue.put(result)
        return result
