from src.agents.coordination import CoordinationAgent

def test_coordination():
    agent = CoordinationAgent()
    agent.receive("Test message")
    assert "Test message" 
