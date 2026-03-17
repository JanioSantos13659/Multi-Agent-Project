import queue
from pathlib import Path

from src.agents.coordination import CoordinationAgent
from src.agents.inventory import InventoryAgent
from src.agents.quotation import QuotationAgent
from src.agents.sales import SalesAgent
from src.helpers.utils import load_dataset

def test_coordination_agent():
    coord_queue = queue.Queue()
    agent = CoordinationAgent()

    # Simula mensagens recebidas
    coord_queue.put("Task 'X' completed")
    coord_queue.put("Resource 'Y' delivered")

    agent.receive(coord_queue)

    assert "Task 'X' completed" in agent.updates
    assert "Resource 'Y' delivered" in agent.updates


def test_coordination_agent_distributes_order_to_sales_agents():
    inventory_agent = InventoryAgent(initial_stock={"A4": 500})
    quotation_agent = QuotationAgent(price_table={"A4": 0.5})
    sales_agent = SalesAgent()
    coordination_agent = CoordinationAgent(inventory_agent, quotation_agent, sales_agent)

    order = {"client": "Empresa X", "quantity": 100, "paper_type": "A4"}
    result = coordination_agent.distribute_order(order)

    assert result["status"] == "completed"
    assert result["proposal"]["total"] == 50.0
    assert result["transaction"]["status"] == "confirmed"


def test_coordination_agent_simulates_dataset_driven_flow():
    dataset_path = Path(__file__).resolve().parents[1] / "data" / "orders.json"
    dataset = load_dataset(str(dataset_path))

    inventory_agent = InventoryAgent(initial_stock={"A4": 1000, "Carta": 1000})
    quotation_agent = QuotationAgent()
    sales_agent = SalesAgent()
    coordination_agent = CoordinationAgent(inventory_agent, quotation_agent, sales_agent)

    for order in dataset:
        coordination_agent.distribute_order(order)

    assert len(sales_agent.transactions) == 2
    assert sales_agent.transactions[0]["client"] == "Empresa X"
    assert sales_agent.transactions[1]["client"] == "Empresa Y"


def test_coordination_agent_returns_out_of_stock_when_inventory_is_insufficient():
    inventory_agent = InventoryAgent(initial_stock={"A4": 10})
    quotation_agent = QuotationAgent(price_table={"A4": 1.0})
    sales_agent = SalesAgent()
    coordination_agent = CoordinationAgent(inventory_agent, quotation_agent, sales_agent)

    order = {"client": "Empresa X", "quantity": 100, "paper_type": "A4"}
    result = coordination_agent.distribute_order(order)

    assert result["status"] == "out_of_stock"
    assert len(sales_agent.transactions) == 0
