import json

import pytest

from src.utils import format_message, load_dataset, validate_input


def test_validate_input_returns_cleaned_string():
    assert validate_input("  ok  ") == "ok"


def test_validate_input_rejects_empty_string():
    with pytest.raises(ValueError):
        validate_input("   ")


def test_format_message_builds_standard_output():
    result = format_message("Task", "Analyze data", "completed")

    assert result == "Task 'Analyze data' completed"


def test_load_dataset_reads_json(tmp_path):
    file_path = tmp_path / "sample.json"
    payload = {"items": [1, 2, 3]}
    file_path.write_text(json.dumps(payload), encoding="utf-8")

    loaded = load_dataset(str(file_path))

    assert loaded == payload


def test_load_dataset_reads_csv(tmp_path):
    file_path = tmp_path / "sample.csv"
    file_path.write_text("name,value\nCPU,4\nRAM,16\n", encoding="utf-8")

    loaded = load_dataset(str(file_path))

    assert loaded == [
        {"name": "CPU", "value": "4"},
        {"name": "RAM", "value": "16"},
    ]


def test_load_dataset_rejects_unsupported_extension(tmp_path):
    file_path = tmp_path / "sample.txt"
    file_path.write_text("content", encoding="utf-8")

    with pytest.raises(ValueError):
        load_dataset(str(file_path))


def test_load_dataset_rejects_missing_file(tmp_path):
    missing_path = tmp_path / "missing.json"

    with pytest.raises(FileNotFoundError):
        load_dataset(str(missing_path))
