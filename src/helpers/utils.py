import json
from pathlib import Path
from typing import Any


def validate_order(order: dict[str, Any]) -> dict[str, Any]:
    """Validate required order fields and normalize text values."""
    if not isinstance(order, dict):
        raise ValueError("order must be a dictionary")

    required_fields = ["client", "quantity", "paper_type"]
    for field in required_fields:
        if field not in order:
            raise ValueError(f"missing required field: {field}")

    client = str(order["client"]).strip()
    paper_type = str(order["paper_type"]).strip()
    quantity = order["quantity"]

    if not client:
        raise ValueError("client cannot be empty")
    if not paper_type:
        raise ValueError("paper_type cannot be empty")
    if not isinstance(quantity, int) or quantity <= 0:
        raise ValueError("quantity must be a positive integer")

    return {
        "client": client,
        "quantity": quantity,
        "paper_type": paper_type,
    }


def calculate_discount(quantity: int) -> float:
    """Return discount rate based on ordered quantity."""
    if quantity >= 500:
        return 0.10
    if quantity >= 200:
        return 0.05
    return 0.0


def format_output(message: str, payload: Any) -> str:
    """Build standardized output message for logs and responses."""
    return f"{message}: {payload}"


def load_dataset(file_path: str) -> Any:
    """Load JSON dataset from disk."""
    dataset_path = Path(file_path)

    if not dataset_path.exists() or not dataset_path.is_file():
        raise FileNotFoundError(f"Dataset not found: {dataset_path}")

    if dataset_path.suffix.lower() != ".json":
        raise ValueError("Unsupported dataset format. Use .json")

    with dataset_path.open("r", encoding="utf-8") as file:
        return json.load(file)
