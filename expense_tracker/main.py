import argparse
from expense_tracker.expenses import add_expense


def main():
    parser = argparse.ArgumentParser(prog="expense-tracker")
    sub = parser.add_subparsers(dest="command")

    add = sub.add_parser("add", help="Add a new expense")
    add.add_argument("--amount", type=float, required=True)
    add.add_argument("--category", required=True)
    add.add_argument("--note", default="")
    add.add_argument("--date", default=None)

    args = parser.parse_args()
    if args.command == "add":
        e = add_expense(args.amount, args.category, args.note, args.date)
        print(f"Added expense #{e['id']}: {e['amount']:.2f} ({e['category']})")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()