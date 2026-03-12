from src.agentes.tarefa import AgenteTarefa

def test_tarefa():
    agente = AgenteTarefa()
    resultado = agente.processar("Teste")
    assert "concluída" in resultado
