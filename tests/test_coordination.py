import queue
from src.agents.coordination import CoordinationAgent

def test_coordination_agent():
    coord_queue = queue.Queue()
    agent = CoordinationAgent()

    # Simula mensagens recebidas
    coord_queue.put("Task 'X' completed")
    coord_queue.put("Resource 'Y' delivered")

    agent.receive(coord_queue)

    assert "Task 'X' completed" in agent.updates
    assert "Resource 'Y' delivered" in agent.updates
