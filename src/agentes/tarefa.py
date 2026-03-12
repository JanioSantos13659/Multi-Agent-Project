import time

class AgenteTarefa:
    def processar(self, tarefa):
        print(f"[Tarefa] Processando: {tarefa}")
        time.sleep(1)
        return f"Tarefa '{tarefa}' concluída"
