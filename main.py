from user_management import login, reset_password
from category_management import add_category, remove_category
from transaction_management import add_transaction
from reporting import generate_report
from budgeting import set_budget, check_budget_exceeded

def main():
    print("Welcome to Expense Manager!")

    if not login():
        print("Incorrect password!")
        return

    while True:
        print("\nOptions:")
        print("1. Add Income Category")
        print("2. Add Expense Category")
        print("3. Add Income")
        print("4. Add Expense")
        print("5. Generate Report")
        print("6. Set Monthly Budget")
        print("7. Exit")
        
        choice = int(input("Enter your choice: "))

        if choice == 1:
            category_name = input("Enter Income Category: ")
            add_category("income", category_name)
        elif choice == 2:
            category_name = input("Enter Expense Category: ")
            add_category("expense", category_name)
        elif choice == 3:
            amount = float(input("Enter Amount: "))
            place = input("Enter Place: ")
            category = input("Enter Category: ")
            add_transaction("income", amount, place, category)
        elif choice == 4:
            amount = float(input("Enter Amount: "))
            place = input("Enter Place: ")
            category = input("Enter Category: ")
            add_transaction("expense", amount, place, category)
            if check_budget_exceeded():
                print("\033[91mBudget Exceeded!\033[0m")
        elif choice == 5:
            report_type = input("Enter Report Type (income/expense): ")
            start_date = input("Enter Start Date (YYYY-MM-DD): ")
            end_date = input("Enter End Date (YYYY-MM-DD): ")
            generate_report(report_type, start_date, end_date)
        elif choice == 6:
            budget = float(input("Enter Monthly Budget: "))
            set_budget(budget)
        elif choice == 7:
            break

if __name__ == "__main__":
    main()
