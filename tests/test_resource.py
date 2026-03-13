import queue
import pytest
from src.agents.resource import ResourceAgent


def test_resource_agent():
    coord_queue = queue.Queue()
    agent = ResourceAgent()
    returned = agent.act("Test Resource", coord_queue)

    queued_result = coord_queue.get()

    assert returned == "Resource 'Test Resource' delivered"
    assert queued_result == "Resource 'Test Resource' delivered"
    assert returned == queued_result


def test_resource_agent_provide_returns_expected_message():
    agent = ResourceAgent()

    result = agent.provide("GPU Cluster")

    assert result == "Resource 'GPU Cluster' delivered"


def test_resource_agent_provide_strips_input_before_formatting():
    agent = ResourceAgent()

    result = agent.provide("  Server A  ")

    assert result == "Resource 'Server A' delivered"


def test_resource_agent_provide_rejects_invalid_input():
    agent = ResourceAgent()

    with pytest.raises(ValueError):
        agent.provide("   ")

