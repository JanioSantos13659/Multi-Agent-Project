import time

class AgenteRecurso:
    def fornecer(self, recurso):
        print(f"[Recurso] Fornecendo: {recurso}")
        time.sleep(1)
        return f"Recurso '{recurso}' entregue"
