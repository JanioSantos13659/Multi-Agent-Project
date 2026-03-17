from pathlib import Path

try:
    from src.agents.coordination import CoordinationAgent
    from src.agents.inventory import InventoryAgent
    from src.agents.quotation import QuotationAgent
    from src.agents.sales import SalesAgent
    from src.helpers.utils import load_dataset
except ModuleNotFoundError:
    from agents.coordination import CoordinationAgent
    from agents.inventory import InventoryAgent
    from agents.quotation import QuotationAgent
    from agents.sales import SalesAgent
    from helpers.utils import load_dataset

def main():
    inventory_agent = InventoryAgent()
    quotation_agent = QuotationAgent()
    sales_agent = SalesAgent()
    coord_agent = CoordinationAgent(inventory_agent, quotation_agent, sales_agent)
    dataset_path = Path(__file__).resolve().parents[1] / "data" / "orders.json"
    orders = load_dataset(str(dataset_path))

    for order in orders:
        coord_agent.distribute_order(order)

    coord_agent.respond_user()

if __name__ == "__main__":
    main()
