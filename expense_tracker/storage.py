import json
from pathlib import Path

DATA_FILE = Path("expenses.json")


def load_expenses(path=DATA_FILE):
    if not path.exists():
        return []
    with open(path, "r") as f:
        return json.load(f)


def save_expenses(expenses, path=DATA_FILE):
    with open(path, "w") as f:
        json.dump(expenses, f, indent=2)