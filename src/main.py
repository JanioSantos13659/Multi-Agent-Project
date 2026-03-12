from agentes.tarefa import AgenteTarefa
from agentes.recurso import AgenteRecurso
from agentes.coordenacao import AgenteCoordenacao

def main():
    tarefa = AgenteTarefa()
    recurso = AgenteRecurso()
    coordenacao = AgenteCoordenacao()

    # Simulação de entrada do usuário
    tarefas = ["Analisar dados", "Gerar relatório"]
    recursos = ["CPU extra", "Memória RAM"]

    for t in tarefas:
        resultado = tarefa.processar(t)
        coordenacao.receber(resultado)

    for r in recursos:
        resultado = recurso.fornecer(r)
        coordenacao.receber(resultado)

    coordenacao.responder_usuario()

if __name__ == "__main__":
    main()
