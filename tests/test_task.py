from src.agents.task import TaskAgent

def test_task():
    agent = TaskAgent()
    result = agent.process("Test")
    assert "completed" in result