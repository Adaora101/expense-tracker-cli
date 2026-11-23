import sys

from expense_tracker.main import main


def run_cli(monkeypatch, *args):
    monkeypatch.setattr(sys, "argv", ["expense-tracker", *args])
    main()


def test_add_command_prints_confirmation(monkeypatch, tmp_path, capsys):
    monkeypatch.chdir(tmp_path)
    run_cli(monkeypatch, "add", "--amount", "12.50", "--category", "food", "--note", "Lunch")
    assert "Added expense #1" in capsys.readouterr().out


def test_add_command_rejects_negative_amount(monkeypatch, tmp_path, capsys):
    monkeypatch.chdir(tmp_path)
    run_cli(monkeypatch, "add", "--amount=-5", "--category", "food")
    assert "Error" in capsys.readouterr().out


def test_list_command_when_empty(monkeypatch, tmp_path, capsys):
    monkeypatch.chdir(tmp_path)
    run_cli(monkeypatch, "list")
    assert "No expenses recorded yet." in capsys.readouterr().out


def test_list_command_shows_expenses(monkeypatch, tmp_path, capsys):
    monkeypatch.chdir(tmp_path)
    run_cli(monkeypatch, "add", "--amount", "8", "--category", "travel")
    capsys.readouterr()
    run_cli(monkeypatch, "list")
    out = capsys.readouterr().out
    assert "travel" in out
    assert "8.00" in out


def test_list_command_handles_corrupted_file(monkeypatch, tmp_path, capsys):
    monkeypatch.chdir(tmp_path)
    (tmp_path / "expenses.json").write_text("{not valid json")
    run_cli(monkeypatch, "list")
    assert "corrupted" in capsys.readouterr().out


def test_delete_command_removes_expense(monkeypatch, tmp_path, capsys):
    monkeypatch.chdir(tmp_path)
    run_cli(monkeypatch, "add", "--amount", "5", "--category", "food")
    capsys.readouterr()
    run_cli(monkeypatch, "delete", "1")
    assert "Deleted expense #1" in capsys.readouterr().out


def test_delete_command_unknown_id(monkeypatch, tmp_path, capsys):
    monkeypatch.chdir(tmp_path)
    run_cli(monkeypatch, "delete", "999")
    assert "Error" in capsys.readouterr().out


def test_no_command_prints_help(monkeypatch, tmp_path, capsys):
    monkeypatch.chdir(tmp_path)
    run_cli(monkeypatch)
    assert "usage" in capsys.readouterr().out.lower()

def test_edit_command_updates_expense(monkeypatch, tmp_path, capsys):
    monkeypatch.chdir(tmp_path)
    run_cli(monkeypatch, "add", "--amount", "5", "--category", "food")
    capsys.readouterr()
    run_cli(monkeypatch, "edit", "1", "--amount", "20")
    assert "Updated expense #1" in capsys.readouterr().out
    run_cli(monkeypatch, "list")
    assert "20.00" in capsys.readouterr().out


def test_edit_command_with_no_fields(monkeypatch, tmp_path, capsys):
    monkeypatch.chdir(tmp_path)
    run_cli(monkeypatch, "edit", "1")
    assert "Nothing to edit" in capsys.readouterr().out


def test_edit_command_unknown_id(monkeypatch, tmp_path, capsys):
    monkeypatch.chdir(tmp_path)
    run_cli(monkeypatch, "edit", "999", "--amount", "5")
    assert "Error" in capsys.readouterr().out