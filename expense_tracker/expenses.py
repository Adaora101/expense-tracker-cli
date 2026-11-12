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