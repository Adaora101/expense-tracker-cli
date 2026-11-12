from datetime import date, datetime
from expense_tracker.storage import load_expenses, save_expenses



def validate_amount(amount):
    try:
        value = float(amount)
    except (TypeError, ValueError):
        raise ValueError("Amount must be a number.")
    if value <= 0:
        raise ValueError("Amount must be greater than zero.")
    return value


def validate_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
    except (TypeError, ValueError):
        raise ValueError("Date must be in YYYY-MM-DD format.")
    return date_str


def add_expense(amount, category, note="", expense_date=None, path=None):
    amount = validate_amount(amount)
    if expense_date:
        validate_date(expense_date)
    kwargs = {"path": path} if path else {}
    expenses = load_expenses(**kwargs)
    new_id = max((e["id"] for e in expenses), default=0) + 1
    expense = {
        "id": new_id,
        "amount": amount,
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