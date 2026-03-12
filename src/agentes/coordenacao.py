class AgenteCoordenacao:
    def __init__(self):
        self.atualizacoes = []

    def receber(self, mensagem):
        print(f"[Coordenação] Atualização recebida: {mensagem}")
        self.atualizacoes.append(mensagem)

    def responder_usuario(self):
        print("[Coordenação] Resposta final ao usuário:")
        for msg in self.atualizacoes:
            print(" -", msg)
