from datetime import date
from expense_tracker.storage import load_expenses, save_expenses


def add_expense(amount, category, note="", expense_date=None, path=None):
    kwargs = {"path": path} if path else {}
    expenses = load_expenses(**kwargs)
    new_id = max((e["id"] for e in expenses), default=0) + 1
    expense = {
        "id": new_id,
        "amount": float(amount),
        "category": category,
        "note": note,
        "date": expense_date or date.today().isoformat(),
    }
    expenses.append(expense)
    save_expenses(expenses, **kwargs)
    return expense
def list_expenses(path=None):
    kwargs = {"path": path} if path else {}
    return load_expenses(**kwargs)
def delete_expense(expense_id, path=None):
    kwargs = {"path": path} if path else {}
    expenses = load_expenses(**kwargs)
    remaining = [e for e in expenses if e["id"] != expense_id]
    if len(remaining) == len(expenses):
        raise ValueError(f"No expense found with ID {expense_id}")
    save_expenses(remaining, **kwargs)