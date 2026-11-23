"""Expense logic for the Expense Tracker CLI.

Description: Add, list, edit, delete and summarise expenses.
Author: YOUR NAME
Version: 1.0
"""

from datetime import date, datetime

from expense_tracker.storage import load_expenses, save_expenses


def validate_amount(amount):
    """Check that an amount is a number greater than zero.

    Args:
        amount: The value to check (number or numeric string).

    Returns:
        float: The amount as a float.

    Raises:
        ValueError: If the amount is not a number or is not above zero.
    """
    try:
        value = float(amount)
    except (TypeError, ValueError):
        raise ValueError("Amount must be a number.")
    if value <= 0:
        raise ValueError("Amount must be greater than zero.")
    return value


def validate_date(date_str):
    """Check that a date string is in YYYY-MM-DD format.

    Args:
        date_str: The date string to check.

    Returns:
        str: The same date string if it is valid.

    Raises:
        ValueError: If the string is not a valid YYYY-MM-DD date.
    """
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
    except (TypeError, ValueError):
        raise ValueError("Date must be in YYYY-MM-DD format.")
    return date_str


def add_expense(amount, category, note="", expense_date=None, path=None):
    """Add a new expense and save it to the data file.

    Args:
        amount: The cost of the expense (must be above zero).
        category: A label such as "food" or "travel".
        note: Optional free-text note.
        expense_date: Optional date as YYYY-MM-DD. Defaults to today.
        path: Optional data file path, used by the tests.

    Returns:
        dict: The new expense, including its unique ID.

    Raises:
        ValueError: If the amount or date is invalid.
    """
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
    """Return all saved expenses.

    Args:
        path: Optional data file path, used by the tests.

    Returns:
        list: A list of expense dictionaries (empty if none exist).
    """
    kwargs = {"path": path} if path else {}
    return load_expenses(**kwargs)


def delete_expense(expense_id, path=None):
    """Delete an expense by its ID.

    Args:
        expense_id: The ID of the expense to remove.
        path: Optional data file path, used by the tests.

    Raises:
        ValueError: If no expense has that ID.
    """
    kwargs = {"path": path} if path else {}
    expenses = load_expenses(**kwargs)
    remaining = [e for e in expenses if e["id"] != expense_id]
    if len(remaining) == len(expenses):
        raise ValueError(f"No expense found with ID {expense_id}")
    save_expenses(remaining, **kwargs)


def edit_expense(expense_id, amount=None, category=None, note=None,
                 expense_date=None, path=None):
    """Update selected fields of an existing expense.

    Only the fields that are given are changed.

    Args:
        expense_id: The ID of the expense to edit.
        amount: Optional new amount.
        category: Optional new category.
        note: Optional new note.
        expense_date: Optional new date as YYYY-MM-DD.
        path: Optional data file path, used by the tests.

    Returns:
        dict: The updated expense.

    Raises:
        ValueError: If the ID is unknown or a new value is invalid.
    """
    kwargs = {"path": path} if path else {}
    if amount is not None:
        amount = validate_amount(amount)
    if expense_date is not None:
        validate_date(expense_date)
    expenses = load_expenses(**kwargs)
    for expense in expenses:
        if expense["id"] == expense_id:
            if amount is not None:
                expense["amount"] = amount
            if category is not None:
                expense["category"] = category
            if note is not None:
                expense["note"] = note
            if expense_date is not None:
                expense["date"] = expense_date
            save_expenses(expenses, **kwargs)
            return expense
    raise ValueError(f"No expense found with ID {expense_id}")


def summarise_by_category(path=None):
    """Total the spending for each category.

    Args:
        path: Optional data file path, used by the tests.

    Returns:
        dict: Maps each category name to its total, rounded to 2 decimals.
    """
    kwargs = {"path": path} if path else {}
    totals = {}
    for expense in load_expenses(**kwargs):
        category = expense["category"]
        totals[category] = totals.get(category, 0) + expense["amount"]
    return {category: round(total, 2) for category, total in totals.items()}