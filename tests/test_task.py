import queue
from src.agents.task import TaskAgent

def test_task_agent():
    coord_queue = queue.Queue()
    agent = TaskAgent()
    agent.act("Test Task", coord_queue)

    result = coord_queue.get()
    assert "completed" in result
