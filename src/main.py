from pathlib import Path

try:
    from src.agents.task import TaskAgent
    from src.agents.resource import ResourceAgent
    from src.agents.coordination import CoordinationAgent
    from src.utils import load_dataset
except ModuleNotFoundError:
    from agents.task import TaskAgent
    from agents.resource import ResourceAgent
    from agents.coordination import CoordinationAgent
    from utils import load_dataset

def main():
    task_agent = TaskAgent()
    resource_agent = ResourceAgent()
    coord_agent = CoordinationAgent()
    dataset_path = Path(__file__).resolve().parents[1] / "tasks.json"
    dataset = load_dataset(str(dataset_path))

    requests = []
    for item in dataset:
        requests.append({"type": "task", "payload": item["task"]})
        requests.append({"type": "resource", "payload": item["resource"]})

    # Coordination routes all dataset-driven requests to specialized agents.
    coord_agent.distribute(requests, task_agent, resource_agent)
    coord_agent.respond_user()

if __name__ == "__main__":
    main()
