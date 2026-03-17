# Project Reflection Report

## What Was Done

The project was evolved into a multi-agent sales workflow that simulates operations of a paper company with reusable helpers and automated validation.

Main implementation work:

- Implemented `InventoryAgent` to control paper stock, availability checks, stock updates, and item reservations.
- Implemented `QuotationAgent` to calculate prices by quantity, apply discount rules, and generate sales proposals.
- Implemented `SalesAgent` to confirm orders, register transactions, and update sale status.
- Adjusted `CoordinationAgent` to receive customer orders and orchestrate inventory, quotation, and sales decisions.
- Added helper utilities in `src/helpers/utils.py`:
  - `validate_order()` for order validation.
  - `calculate_discount()` for quantity discount policy.
  - `format_output()` for standardized workflow messages.
  - `load_dataset()` for order dataset loading.
- Added a dedicated order dataset:
  - `data/orders.json`
- Added tests for each sales-focused agent and coordination flow.

## Difficulties

The most relevant difficulties were:

- Defining clear boundaries between the three sales agents so each one has a single responsibility.
- Guaranteeing consistent order validation in every part of the flow.
- Designing discount and pricing behavior simple enough for tests, but realistic for a paper sales scenario.

## How the Agents Simulate Paper Sales Flow

The system simulates daily paper sales by splitting responsibilities into specialized agents coordinated by a central orchestrator:

- `InventoryAgent` focuses on stock accuracy and reservation safety.
- `QuotationAgent` focuses on pricing policy and discount transparency.
- `SalesAgent` focuses on final commercial confirmation and transaction lifecycle.
- `CoordinationAgent` orchestrates the complete journey from request to sale completion.

Typical flow:

1. A customer order arrives with client, paper type, and quantity.
2. `CoordinationAgent` validates and distributes the order.
3. `InventoryAgent` checks and reserves stock.
4. `QuotationAgent` generates a proposal with subtotal, discount, and final total.
5. `SalesAgent` confirms and records the transaction status.
6. `CoordinationAgent` returns a consolidated result and audit trail.

This architecture improves organization and transparency because each business step is explicit, traceable, and testable.

## Future Improvements

Potential next steps:

- Add customer-specific pricing rules and contract-based discount tiers.
- Persist transactions to a database for full commercial history.
- Include invoice generation and payment tracking status transitions.
- Add dashboards for stock visibility and quotation conversion rate.
