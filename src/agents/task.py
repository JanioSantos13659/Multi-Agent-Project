import time


class TaskAgent:
    def process(self, task):
        print(f"[Task] Processing: {task}")
        time.sleep(1)
        return f"Task '{task}' completed"

    # Backward compatibility with existing Portuguese method calls.
    def processar(self, tarefa):
        return self.process(tarefa)


# Backward compatibility with existing Portuguese class imports.
AgenteTarefa = TaskAgent
