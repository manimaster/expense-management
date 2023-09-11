import json
import datetime

def add_transaction(transaction_type, amount, place, category):
    transaction = {
        "type": transaction_type,
        "amount": amount,
        "place": place,
        "date": str(datetime.date.today()),
        "time": str(datetime.datetime.now().time()),
        "category": category
    }
    
    with open('transactions.json', 'a') as f:
        json.dump(transaction, f)
        f.write("\n")
