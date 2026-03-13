import queue
from pathlib import Path

import pytest
from src.agents.task import TaskAgent
from src.utils import load_dataset


def test_task_agent():
    coord_queue = queue.Queue()
    agent = TaskAgent()
    agent.act("Test Task", coord_queue)

    result = coord_queue.get()
    assert "completed" in result


def test_task_agent_process_returns_expected_message():
    agent = TaskAgent()

    result = agent.process("Analyze report")

    assert result == "Task 'Analyze report' completed"


def test_task_agent_process_rejects_invalid_input():
    agent = TaskAgent()

    with pytest.raises(ValueError):
        agent.process("   ")


def test_task_agent_processes_dataset_tasks_correctly():
    dataset_path = Path(__file__).resolve().parents[1] / "tasks.json"
    dataset = load_dataset(str(dataset_path))
    agent = TaskAgent()

    results = [agent.process(item["task"]) for item in dataset]

    assert results == [
        "Task 'Backup database' completed",
        "Task 'Generate report' completed",
    ]
