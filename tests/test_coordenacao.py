from src.agentes.coordenacao import AgenteCoordenacao

def test_coordenacao():
    agente = AgenteCoordenacao()
    agente.receber("Mensagem de teste")
    assert "Mensagem de teste" in agente.atualizacoes
