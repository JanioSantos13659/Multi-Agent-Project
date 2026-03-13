import queue
from agents.task import TaskAgent
from agents.resource import ResourceAgent
from agents.coordination import CoordinationAgent

def main():
    coord_queue = queue.Queue()
    task_agent = TaskAgent()
    resource_agent = ResourceAgent()
    coord_agent = CoordinationAgent()

    # User requests
    task_agent.act("Analyze data", coord_queue)
    resource_agent.act("Extra CPU", coord_queue)

    # Coordination receives and responds
    coord_agent.receive(coord_queue)
    coord_agent.respond_user()

if __name__ == "__main__":
    main()
