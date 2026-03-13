class CoordinationAgent:
    def __init__(self):
        self.updates = []

    def receive(self, message):
        print(f"[Coordination] Update received: {message}")
        self.updates.append(message)

    def respond_to_user(self):
        print("[Coordination] Final response to user:")
        for msg in self.updates:
            print(" -", msg)

    # Backward compatibility with existing Portuguese method calls.
    def receber(self, mensagem):
        self.receive(mensagem)

    def responder_usuario(self):
        self.respond_to_user()


# Backward compatibility with existing Portuguese class imports.
AgenteCoordenacao = CoordinationAgent
