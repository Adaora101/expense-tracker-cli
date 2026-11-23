import pytest
from expense_tracker.storage import load_expenses, save_expenses


def test_load_returns_empty_list_when_file_missing(tmp_path):
    assert load_expenses(tmp_path / "missing.json") == []


def test_save_then_load_round_trip(tmp_path):
    data_file = tmp_path / "data.json"
    data = [{"id": 1, "amount": 5.0}]
    save_expenses(data, data_file)
    assert load_expenses(data_file) == data


def test_corrupted_file_raises_value_error(tmp_path):
    data_file = tmp_path / "bad.json"
    data_file.write_text("{not valid json")
    with pytest.raises(ValueError):
        load_expenses(data_file)