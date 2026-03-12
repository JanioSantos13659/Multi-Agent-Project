from src.agentes.recurso import AgenteRecurso

def test_recurso():
    agente = AgenteRecurso()
    resultado = agente.fornecer("Teste")
    assert "entregue" in resultado
