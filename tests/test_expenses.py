from datetime import date

import pytest
from expense_tracker.expenses import add_expense, list_expenses, delete_expense, edit_expense


def test_add_expense_saves_to_file(tmp_path):
    data_file = tmp_path / "test.json"
    add_expense(12.5, "food", "Lunch", path=data_file)
    expenses = list_expenses(path=data_file)
    assert len(expenses) == 1
    assert expenses[0]["category"] == "food"
    assert expenses[0]["amount"] == 12.5


def test_add_expense_assigns_incrementing_ids(tmp_path):
    data_file = tmp_path / "test.json"
    first = add_expense(1, "food", path=data_file)
    second = add_expense(2, "food", path=data_file)
    assert first["id"] == 1
    assert second["id"] == 2


def test_add_expense_defaults_to_today(tmp_path):
    data_file = tmp_path / "test.json"
    expense = add_expense(5, "travel", path=data_file)
    assert expense["date"] == date.today().isoformat()


def test_add_expense_rejects_negative_amount(tmp_path):
    with pytest.raises(ValueError):
        add_expense(-5, "food", path=tmp_path / "test.json")


def test_add_expense_rejects_invalid_date(tmp_path):
    with pytest.raises(ValueError):
        add_expense(5, "food", expense_date="2026-13-45", path=tmp_path / "test.json")


def test_list_expenses_empty_when_no_file(tmp_path):
    assert list_expenses(path=tmp_path / "none.json") == []


def test_delete_expense_removes_it(tmp_path):
    data_file = tmp_path / "test.json"
    add_expense(10, "food", path=data_file)
    delete_expense(1, path=data_file)
    assert list_expenses(path=data_file) == []


def test_delete_unknown_id_raises_error(tmp_path):
    with pytest.raises(ValueError):
        delete_expense(999, path=tmp_path / "test.json")


def test_edit_expense_updates_only_given_fields(tmp_path):
    data_file = tmp_path / "test.json"
    add_expense(10, "food", "Lunch", path=data_file)
    edit_expense(1, amount=15, path=data_file)
    expense = list_expenses(path=data_file)[0]
    assert expense["amount"] == 15
    assert expense["category"] == "food"
    assert expense["note"] == "Lunch"


def test_edit_expense_unknown_id_raises_error(tmp_path):
    with pytest.raises(ValueError):
        edit_expense(999, amount=5, path=tmp_path / "test.json")


def test_edit_expense_rejects_invalid_amount(tmp_path):
    data_file = tmp_path / "test.json"
    add_expense(10, "food", path=data_file)
    with pytest.raises(ValueError):
        edit_expense(1, amount=-3, path=data_file)