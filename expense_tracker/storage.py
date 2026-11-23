"""Storage helpers for the Expense Tracker CLI.

Description: Load and save expenses to a JSON file.
Author: Adaora Obialo
Version: 1.0
"""
import json
from pathlib import Path

DATA_FILE = Path("expenses.json")


def load_expenses(path=DATA_FILE):
    """Load expenses from a JSON file. Returns [] if missing; raises ValueError if corrupted."""
    if not path.exists():
        return []
    try:
        with open(path, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        raise ValueError(f"Data file {path} is corrupted. Fix or delete it.")


def save_expenses(expenses, path=DATA_FILE):
    """Write the list of expenses to a JSON file."""
    with open(path, "w") as f:
        json.dump(expenses, f, indent=2)