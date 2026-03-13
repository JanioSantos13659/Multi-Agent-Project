from agents.task import TaskAgent
from agents.resource import ResourceAgent
from agents.coordination import CoordinationAgent


def main():
    task_agent = TaskAgent()
    resource_agent = ResourceAgent()
    coordination_agent = CoordinationAgent()

    # Simulated user input.
    tasks = ["Analyze data", "Generate report"]
    resources = ["Extra CPU", "RAM memory"]

    for task in tasks:
        result = task_agent.process(task)
        coordination_agent.receive(result)

    for resource in resources:
        result = resource_agent.provide(resource)
        coordination_agent.receive(result)

    coordination_agent.respond_to_user()


if __name__ == "__main__":
    main()
