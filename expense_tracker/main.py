"""Command-line entry point for the Expense Tracker CLI.

Description: Parses commands (add, list, delete, edit, summary) and runs them.
Author: Adaora Obialo
Version: 1.0
"""
import argparse
from expense_tracker.expenses import (
    add_expense,
    list_expenses,
    delete_expense,
    edit_expense,
    summarise_by_category,
)


def main():
    """Parse command-line arguments and run the chosen command."""
    parser = argparse.ArgumentParser(prog="expense-tracker")
    sub = parser.add_subparsers(dest="command")

    add = sub.add_parser("add", help="Add a new expense")
    add.add_argument("--amount", type=float, required=True)
    add.add_argument("--category", required=True)
    add.add_argument("--note", default="")
    add.add_argument("--date", default=None)

    sub.add_parser("list", help="List all expenses")

    delete = sub.add_parser("delete", help="Delete an expense by ID")
    delete.add_argument("id", type=int)

    edit = sub.add_parser("edit", help="Edit an existing expense")
    edit.add_argument("id", type=int)
    edit.add_argument("--amount", type=float, default=None)
    edit.add_argument("--category", default=None)
    edit.add_argument("--note", default=None)
    edit.add_argument("--date", default=None)
    sub.add_parser("summary", help="Show total spending by category")

    args = parser.parse_args()
    if args.command == "add":
        try:
            e = add_expense(args.amount, args.category, args.note, args.date)
            print(f"Added expense #{e['id']}: {e['amount']:.2f} ({e['category']})")
        except ValueError as err:
            print(f"Error: {err}")
    elif args.command == "list":
        try:
            expenses = list_expenses()
        except ValueError as err:
            print(f"Error: {err}")
            return
        if not expenses:
            print("No expenses recorded yet.")
        else:
            print(f"{'ID':<4} {'Date':<12} {'Category':<12} {'Amount':>9}  Note")
            for e in expenses:
                print(f"{e['id']:<4} {e['date']:<12} {e['category']:<12} {e['amount']:>9.2f}  {e['note']}")
    elif args.command == "delete":
        try:
            delete_expense(args.id)
            print(f"Deleted expense #{args.id}")
        except ValueError as err:
            print(f"Error: {err}")
    elif args.command == "edit":
        fields = (args.amount, args.category, args.note, args.date)
        if all(f is None for f in fields):
            print("Error: Nothing to edit. Use --amount, --category, --note or --date.")
            return
        try:
            e = edit_expense(args.id, args.amount, args.category, args.note, args.date)
            print(f"Updated expense #{e['id']}")
        except ValueError as err:
            print(f"Error: {err}")
    elif args.command == "summary":
        try:
            totals = summarise_by_category()
        except ValueError as err:
            print(f"Error: {err}")
            return
        if not totals:
            print("No expenses recorded yet.")
        else:
            print(f"{'Category':<15} {'Total':>10}")
            for category, total in sorted(totals.items()):
                print(f"{category:<15} {total:>10.2f}")
            print(f"{'TOTAL':<15} {sum(totals.values()):>10.2f}")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()