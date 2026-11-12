import argparse
from expense_tracker.expenses import add_expense, list_expenses, delete_expense

def main():
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

    args = parser.parse_args()
    if args.command == "add":
        e = add_expense(args.amount, args.category, args.note, args.date)
        print(f"Added expense #{e['id']}: {e['amount']:.2f} ({e['category']})")
    elif args.command == "list":
        expenses = list_expenses()
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
    else:
        parser.print_help()
    


if __name__ == "__main__":
    main()
