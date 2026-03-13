class CoordinationAgent:
    def __init__(self, name="CoordinationAgent"):
        self.name = name
        self.updates = []

    def receive(self, coord_queue):
        while not coord_queue.empty():
            msg = coord_queue.get()
            self.updates.append(msg)
            print(f"[Coordination] {msg}")

    def respond_user(self):
        print("Final response to user:")
        for msg in self.updates:
            print(" -", msg)
