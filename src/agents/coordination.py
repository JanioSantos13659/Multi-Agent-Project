import queue


class CoordinationAgent:
    def __init__(self, name="CoordinationAgent", coord_queue=None):
        self.name = name
        self.coord_queue = coord_queue or queue.Queue()
        self.updates = []

    def receive(self, message_or_queue=None):
        if message_or_queue is None:
            target_queue = self.coord_queue
        elif hasattr(message_or_queue, "empty") and hasattr(message_or_queue, "get"):
            target_queue = message_or_queue
        else:
            self.updates.append(message_or_queue)
            print(f"[Coordination] {message_or_queue}")
            return

        while not target_queue.empty():
            msg = target_queue.get()
            self.updates.append(msg)
            print(f"[Coordination] {msg}")

    def distribute(self, requests, task_agent, resource_agent):
        for request in requests:
            request_type = request.get("type")
            payload = request.get("payload")

            if request_type == "task":
                task_agent.act(payload, self.coord_queue)
            elif request_type == "resource":
                resource_agent.act(payload, self.coord_queue)
            else:
                self.receive(f"Unsupported request type: {request_type}")

        self.receive(self.coord_queue)

    def respond_user(self):
        print("Final response to user:")
        for msg in self.updates:
            print(" -", msg)
