from src.agents.quotation import QuotationAgent


def test_quotation_agent_calculates_price_by_quantity():
    agent = QuotationAgent(price_table={"A4": 0.10})

    total = agent.calculate_price(100, "A4")

    assert total == 10.0


def test_quotation_agent_applies_discount_by_quantity():
    agent = QuotationAgent(price_table={"Carta": 0.20})

    subtotal = agent.calculate_price(250, "Carta")
    total = agent.apply_discounts(subtotal, 250)

    assert subtotal == 50.0
    assert total == 47.5


def test_quotation_agent_generates_complete_proposal():
    agent = QuotationAgent(price_table={"A4": 1.0})
    order = {"client": "Empresa X", "quantity": 250, "paper_type": "A4"}

    proposal = agent.generate_proposal(order)

    assert proposal["client"] == "Empresa X"
    assert proposal["subtotal"] == 250.0
    assert proposal["discount_rate"] == 0.05
    assert proposal["total"] == 237.5
