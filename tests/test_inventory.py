from src.agents.inventory import InventoryAgent


def test_inventory_agent_checks_availability_correctly():
    agent = InventoryAgent(initial_stock={"A4": 120})

    assert agent.check_availability("A4", 100) is True
    assert agent.check_availability("A4", 121) is False


def test_inventory_agent_updates_stock_quantity():
    agent = InventoryAgent(initial_stock={"Carta": 80})

    updated = agent.update_quantity("Carta", 20)

    assert updated == 100
    assert agent.stock["Carta"] == 100


def test_inventory_agent_reserves_items_and_reduces_stock():
    agent = InventoryAgent(initial_stock={"A4": 200})
    order = {"client": "Empresa X", "quantity": 50, "paper_type": "A4"}

    reserved = agent.reserve_items(order)

    assert reserved is True
    assert agent.stock["A4"] == 150
