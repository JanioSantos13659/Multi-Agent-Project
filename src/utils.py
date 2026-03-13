import csv
import json
from pathlib import Path
from typing import Any


def log(message: str) -> None:
    """Print a formatted log message."""
    print(f"[LOG] {message}")


def validate_input(value: str, field_name: str = "input") -> str:
    """Validate and normalize text input by trimming whitespace."""
    if not isinstance(value, str):
        raise ValueError(f"{field_name} must be a string")

    cleaned_value = value.strip()
    if not cleaned_value:
        raise ValueError(f"{field_name} cannot be empty")

    return cleaned_value


def format_message(entity: str, value: str, action: str) -> str:
    """Create a standardized output message used by multiple agents."""
    clean_entity = validate_input(entity, "entity")
    clean_value = validate_input(value, clean_entity.lower())
    clean_action = validate_input(action, "action")

    return f"{clean_entity} '{clean_value}' {clean_action}"


def load_dataset(file_path: str) -> Any:
    """Load dataset content from JSON or CSV files."""
    clean_path = validate_input(file_path, "file_path")
    dataset_path = Path(clean_path)

    if not dataset_path.exists() or not dataset_path.is_file():
        raise FileNotFoundError(f"Dataset not found: {dataset_path}")

    suffix = dataset_path.suffix.lower()
    if suffix == ".json":
        with dataset_path.open("r", encoding="utf-8") as file:
            return json.load(file)

    if suffix == ".csv":
        # DictReader keeps column names as keys for tabular datasets.
        with dataset_path.open("r", encoding="utf-8", newline="") as file:
            return list(csv.DictReader(file))

    raise ValueError("Unsupported dataset format. Use .json or .csv")
