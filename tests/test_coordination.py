import queue
from pathlib import Path

from src.agents.coordination import CoordinationAgent
from src.agents.task import TaskAgent
from src.agents.resource import ResourceAgent
from src.utils import load_dataset

def test_coordination_agent():
    coord_queue = queue.Queue()
    agent = CoordinationAgent()

    # Simula mensagens recebidas
    coord_queue.put("Task 'X' completed")
    coord_queue.put("Resource 'Y' delivered")

    agent.receive(coord_queue)

    assert "Task 'X' completed" in agent.updates
    assert "Resource 'Y' delivered" in agent.updates


def test_coordination_agent_distributes_messages():
    task_agent = TaskAgent()
    resource_agent = ResourceAgent()
    coordination_agent = CoordinationAgent()

    requests = [
        {"type": "task", "payload": "Analyze data"},
        {"type": "resource", "payload": "Extra CPU"},
    ]

    coordination_agent.distribute(requests, task_agent, resource_agent)

    assert "Task 'Analyze data' completed" in coordination_agent.updates
    assert "Resource 'Extra CPU' delivered" in coordination_agent.updates


def test_coordination_agent_simulates_dataset_driven_flow():
    dataset_path = Path(__file__).resolve().parents[1] / "tasks.json"
    dataset = load_dataset(str(dataset_path))

    requests = []
    for item in dataset:
        requests.append({"type": "task", "payload": item["task"]})
        requests.append({"type": "resource", "payload": item["resource"]})

    coordination_agent = CoordinationAgent()
    task_agent = TaskAgent()
    resource_agent = ResourceAgent()

    coordination_agent.distribute(requests, task_agent, resource_agent)

    assert "Task 'Backup database' completed" in coordination_agent.updates
    assert "Resource 'Server A' delivered" in coordination_agent.updates
    assert "Task 'Generate report' completed" in coordination_agent.updates
    assert "Resource 'Server B' delivered" in coordination_agent.updates


def test_coordination_agent_handles_unsupported_request_type():
    coordination_agent = CoordinationAgent()
    task_agent = TaskAgent()
    resource_agent = ResourceAgent()

    requests = [
        {"type": "task", "payload": "Prepare dashboard"},
        {"type": "unknown", "payload": "X"},
    ]

    coordination_agent.distribute(requests, task_agent, resource_agent)

    assert "Task 'Prepare dashboard' completed" in coordination_agent.updates
    assert "Unsupported request type: unknown" in coordination_agent.updates
