import queue
from src.agents.resource import ResourceAgent

def test_resource_agent():
    coord_queue = queue.Queue()
    agent = ResourceAgent()
    agent.act("Test Resource", coord_queue)

    result = coord_queue.get()
    assert "delivered" in result

