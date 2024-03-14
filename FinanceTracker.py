import json
from datetime import datetime

# Global list to store transactions
transactions = []

# File handling functions
def load_transactions():
    global transactions
    try:
        with open('finance-tracker.json', 'r') as file:
            transactions = json.load(file)
    except FileNotFoundError:
        transactions = []
    except json.decoder.JSONDecodeError:
        print("There are no transactions.")
        transactions = []
    print(transactions)

def save_transactions():
    with open('finance-tracker.json', 'w') as file:
        json.dump(transactions, file)

# Feature implementations
def add_transaction():
    
    transaction_amount = validate_amount()
    
    transaction_category = validate_category()

    transaction_type = validate_type()

    transaction_date = validate_date()

    transaction = [transaction_amount, transaction_category, transaction_type, transaction_date]
    transactions.append(transaction)
    print("Transaction added Successfully!")
    save_transactions()

def view_transactions():
    if not transactions:
        print("No transactions found!")
    else:
        print("Transactions:")
        for transaction in transactions:
            print(transaction)


def update_transaction():
    # Placeholder for update transaction logic
    # Remember to use save_transactions() after updating
    view_transactions()
    index = int(input("Enter the index of transaction that you need to change : "))
    if 0 < index <= len(transactions):
        transaction_amount = validate_amount()
    
        transaction_category = validate_category()

        transaction_type = validate_type()

        transaction_date = validate_date()

        transactions[index-1] = [transaction_amount, transaction_category, transaction_type, transaction_date]
        print("Transaction Updates Successfully!")
        save_transactions()
    else: 
        print("Transactions not found!")

def delete_transaction():
    view_transactions()
    # Placeholder for delete transaction logic
    # Remember to use save_transactions() after deleting
    index = int(input("Enter the index of transaction : "))
    while True:
        if 0 <= index <= len(transactions):
            del transactions[index-1]
            print("Transaction deleted successfully!")
            save_transactions()
            break
        else:
            print("Transaction doesn't exist. Please enter a index greater than 0")
            index = int(input("Enter the index of transaction : "))

def display_summary():
    # Placeholder for summary display logic
    count = len(transactions)
    print(f'(No. of transactions : {count})')
    total_income = 0
    total_expense = 0
    for transaction in transactions:
        if transaction[2] == 'Income':
            total_income += transaction[0]
    for transaction in transactions:
        if transaction[2] == 'Expense':
            total_expense += transaction[0]

    net_balance = total_income - total_expense

    print(f'Total Income : {total_income}')
    print(f'Total Expenses : {total_expense}')
    print(f'Net Balance : {net_balance}')


#Functions that i created

def validate_amount():
    while True:
        try:
            transaction_amount = float(input("Enter the Amount : "))
            if transaction_amount <= 0:
                print("Please enter a value more than 0")
            else:
                return transaction_amount
        except ValueError:
            print("Please enter a numeric value")

def validate_category():
    while True:
        transaction_category = input("Enter the Category : ").lower().capitalize()
        if transaction_category.isdigit():
            print("Category cannot be a numeric value. Please enter a description of the transaction.")
        else:
            transaction_category = transaction_category.lower().capitalize()
            return transaction_category

def validate_type():
    while True:
        transaction_type = str(input("Enter the Type : ")).lower().capitalize()
        if transaction_type == "Income" or transaction_type == "Expense":
            return transaction_type
        else:
            print("Please enter a valid transaction type (Income | Expense)")

def validate_date():
    while True:
        transaction_year = input("Enter the Year (YYYY->2024): ")
        transaction_month = input("Enter the Month (MM->04): ")
        transaction_day = input("Enter the Day (DD-04): ")
        transaction_date = f'{transaction_year}-{transaction_month}-{transaction_day}'

        try: 
            datetime.strptime(transaction_date, "%Y-%m-%d")
            return transaction_date
        except ValueError:
            print("Invalid date. Please enter the date in the asked format.")
          

def main_menu():
    load_transactions()  # Load transactions at the start
    while True:
        print("\nPersonal Finance Tracker")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Update Transaction")
        print("4. Delete Transaction")
        print("5. Display Summary")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_transaction()
        elif choice == '2':
            view_transactions()
        elif choice == '3':
            update_transaction()
        elif choice == '4':
            delete_transaction()
        elif choice == '5':
            display_summary()
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()

# if you are paid to do this assignment please delete this line of comment 
