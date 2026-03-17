# Technical Report - Multi-Agent System

## 1. Objective
Document the architecture and operational flow of the multi-agent system represented in the diagram, describing components, interactions, and responsibilities.

## 2. Overview
The system is composed of a coordination agent and three sales-focused specialized agents:

- **InventoryAgent**: manages paper stock, checks availability, and reserves items.
- **QuotationAgent**: calculates prices, applies discounts, and generates proposals.
- **SalesAgent**: confirms orders, registers transactions, and updates sale status.
- **CoordinationAgent**: receives customer orders, orchestrates the flow, and consolidates responses.

## 3. Flow Represented in the Diagram
1. Agent initialization.
2. Customer orders are received by the **CoordinationAgent**.
3. Availability and reservation are handled by the **InventoryAgent**.
4. Pricing and discount rules are applied by the **QuotationAgent**.
5. Order confirmation and transaction registration are handled by the **SalesAgent**.
6. Updates are consolidated and the final sales status is sent to the user.

## 4. Components and Responsibilities

### 4.1 InventoryAgent
- Receives order item and quantity.
- Checks stock availability and reserves paper items.
- Updates stock balances.

### 4.2 QuotationAgent
- Receives validated order data.
- Calculates subtotal by paper type and quantity.
- Applies discount rules and generates final proposal.

### 4.3 SalesAgent
- Confirms order based on stock reservation result.
- Registers sale transaction data.
- Updates sale lifecycle status.

### 4.4 CoordinationAgent
- Receives and validates customer orders.
- Orchestrates Inventory, Quotation, and Sales agents.
- Maintains message history and produces a consolidated response.

## 5. Related Code Structure

```text
src/
|-- agents/
|   |-- coordination.py
|   |-- inventory.py
|   |-- quotation.py
|   `-- sales.py
|-- helpers/
|   `-- utils.py
`-- main.py

data/
`-- orders.json

tests/
|-- test_coordination.py
|-- test_inventory.py
|-- test_quotation.py
`-- test_sales.py
```

## 6. New Files Referenced
- `src/agents/inventory.py`
- `src/agents/quotation.py`
- `src/agents/sales.py`
- `src/agents/coordination.py`
- `src/helpers/utils.py`
- `data/orders.json`
- `tests/test_inventory.py`
- `tests/test_quotation.py`
- `tests/test_sales.py`
- `tests/test_coordination.py`

## 7. Validation
Behavior validation is performed with automated tests (`pytest`), including order simulation using `data/orders.json` and validation of each specialized agent.

## 8. Conclusion
The architecture shown in the diagram highlights separation of responsibilities, transparent sales flow for a paper company, and easier maintenance through clearly scoped agents and tests.