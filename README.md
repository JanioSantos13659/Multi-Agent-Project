<<<<<<< HEAD
# Multiagente Projeto

Projeto em Python para simulação de um sistema multiagente, com agentes especializados para coordenação, tarefas e recursos.

## 📌 Visão geral

O projeto organiza responsabilidades em agentes separados:

- **AgenteCoordenacao**: recebe e centraliza atualizações/mensagens.
- **AgenteTarefa**: representa regras e operações relacionadas a tarefas.
- **AgenteRecurso**: representa regras e operações relacionadas a recursos.

Os comportamentos são validados por testes automatizados com `pytest`.

## 🧱 Estrutura do projeto

```text
multiagente-projeto/
├─ src/
│  ├─ __init__.py
│  └─ agentes/
│     ├─ __init__.py
│     ├─ coordenacao.py
│     ├─ tarefa.py
│     └─ recurso.py
├─ tests/
│  ├─ test_coordenacao.py
│  ├─ test_tarefa.py
│  └─ test_recurso.py
├─ requirements.txt
└─ pytest.ini
```

## ⚙️ Requisitos

- Python 3.11+
- pip
- dependências em `requirements.txt`

## 🚀 Instalação

No terminal (Windows/PowerShell), na raiz do projeto:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## ✅ Executando os testes

```powershell
python -m pytest -q
```

## 🧪 Exemplo de comportamento esperado

No teste de coordenação, ao receber uma mensagem, o agente deve armazená-la em suas atualizações:

- `agente.receber("Mensagem de teste")`
- `"Mensagem de teste"` deve existir em `agente.atualizacoes`

## 🛠️ Tecnologias

- Python
- Pytest

## 📄 Licença

Licença ainda não definida no repositório.
=======
# Multi-Agent-Project
“The Multi-Agent Project builds systems of autonomous agents that collaborate to solve complex tasks, with applications in AI, robotics, and smart environments.
>>>>>>> b2d59b9f75c3040f37a038a488286e39843c44e7
