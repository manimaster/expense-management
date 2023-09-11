from utils import load_config
import json
import datetime

BUDGET_FILE = "monthly_budget.json"

def set_budget(amount):
    budget = {
        "month": datetime.date.today().month,
        "year": datetime.date.today().year,
        "amount": amount
    }

    with open(BUDGET_FILE, 'w') as f:
        json.dump(budget, f)

def get_budget():
    with open(BUDGET_FILE, 'r') as f:
        budget = json.load(f)
    return budget

def check_budget_exceeded():
    budget = get_budget()
    transactions = []
    with open('transactions.json', 'r') as f:
        for line in f:
            transactions.append(json.loads(line))

    current_month_expenses = [t for t in transactions if t["type"] == "expense" and datetime.datetime.strptime(t["date"], '%Y-%m-%d').date().month == budget["month"]]

    total_expense = sum([t["amount"] for t in current_month_expenses])

    return total_expense > budget["amount"]
