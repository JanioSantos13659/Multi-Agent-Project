from src.agents.resource import ResourceAgent

def test_resource():
    agent = ResourceAgent()
    result = agent.provide("Test")
    assert "delivered" in result
