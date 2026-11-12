import json
from pathlib import Path

DATA_FILE = Path("expenses.json")


def load_expenses(path=DATA_FILE):
    if not path.exists():
        return []
    try:
        with open(path, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        raise ValueError(f"Data file {path} is corrupted. Fix or delete it.")


def save_expenses(expenses, path=DATA_FILE):
    with open(path, "w") as f:
        json.dump(expenses, f, indent=2)