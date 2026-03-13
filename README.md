Multiagent Project
Python project for simulating a multiagent system, with specialized agents for coordination, tasks, and resources.

📌 Overview
The project organizes responsibilities into separate agents:

CoordinationAgent: receives and centralizes updates/messages.

TaskAgent: represents rules and operations related to tasks.

ResourceAgent: represents rules and operations related to resources.

Behaviors are validated through automated tests using pytest.

🧱 Project Structure
text
multiagent-project/
├─ src/
│  ├─ __init__.py
│  └─ agents/
│     ├─ __init__.py
│     ├─ coordination.py
│     ├─ task.py
│     └─ resource.py
├─ tests/
│  ├─ test_coordination.py
│  ├─ test_task.py
│  └─ test_resource.py
├─ requirements.txt
└─ pytest.ini
⚙️ Requirements
Python 3.11+

pip

dependencies listed in requirements.txt

🚀 Installation
In the terminal (Windows/PowerShell), at the project root:

powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
✅ Running the tests
powershell
python -m pytest -q
🧪 Example of expected behavior
In the coordination test, when receiving a message, the agent should store it in its updates:

agent.receive("Test message")

"Test message" should exist in agent.updates

🛠️ Technologies
Python

Pytest

📄 License
License not yet defined in the repository.

