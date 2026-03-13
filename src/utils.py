import csv
import json
from pathlib import Path


def log(message):
    print(f"[LOG] {message}")


def validate_input(value, field_name="input"):
    if not isinstance(value, str):
        raise ValueError(f"{field_name} must be a string")

    cleaned_value = value.strip()
    if not cleaned_value:
        raise ValueError(f"{field_name} cannot be empty")

    return cleaned_value


def format_message(entity, value, action):
    clean_entity = validate_input(entity, "entity")
    clean_value = validate_input(value, clean_entity.lower())
    clean_action = validate_input(action, "action")

    return f"{clean_entity} '{clean_value}' {clean_action}"


def load_dataset(file_path):
    clean_path = validate_input(file_path, "file_path")
    dataset_path = Path(clean_path)

    if not dataset_path.exists() or not dataset_path.is_file():
        raise FileNotFoundError(f"Dataset not found: {dataset_path}")

    suffix = dataset_path.suffix.lower()
    if suffix == ".json":
        with dataset_path.open("r", encoding="utf-8") as file:
            return json.load(file)

    if suffix == ".csv":
        with dataset_path.open("r", encoding="utf-8", newline="") as file:
            return list(csv.DictReader(file))

    raise ValueError("Unsupported dataset format. Use .json or .csv")
