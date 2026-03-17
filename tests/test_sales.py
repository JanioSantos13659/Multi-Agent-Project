from src.agents.sales import SalesAgent


def test_sales_agent_confirms_order_when_inventory_reserved():
    agent = SalesAgent()

    assert agent.confirm_order(True) is True
    assert agent.confirm_order(False) is False


def test_sales_agent_registers_transaction_with_confirmed_status():
    agent = SalesAgent()
    proposal = {
        "client": "Empresa X",
        "paper_type": "A4",
        "quantity": 100,
        "total": 90.0,
    }

    transaction = agent.register_transaction(proposal)

    assert transaction["sale_id"] == 1
    assert transaction["status"] == "confirmed"
    assert transaction["total"] == 90.0


def test_sales_agent_updates_sale_status():
    agent = SalesAgent()
    proposal = {
        "client": "Empresa X",
        "paper_type": "A4",
        "quantity": 100,
        "total": 90.0,
    }
    transaction = agent.register_transaction(proposal)

    updated = agent.update_sale_status(transaction["sale_id"], "paid")

    assert updated["status"] == "paid"
