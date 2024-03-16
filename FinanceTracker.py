import json
from datetime import datetime

# Global list to store transactions
transactions = []

# File handling functions
def load_transactions():
    global transactions #Calling the transaction global list for this function coz otherwise it will store the data in a local varibale.
    try:
        with open('finance-tracker.json', 'r') as file:
            transactions = json.load(file) #Loading the json file and assigning the data to thr global list transactions
    except FileNotFoundError: #If there is no such file then the transaction list will be printed.
        transactions = []
    except json.decoder.JSONDecodeError: #If the attempt to decypher the JSON data from the file fails coz of JSON Formatting the below print block will be executed.
        print("There are no transactions.")
        transactions = []
    print(transactions)

def save_transactions():
    with open('finance-tracker.json', 'w') as file:
        json.dump(transactions, file) #Converts the trasaction list to JSON format and transfers the data in the global list transactions into the file.

# Feature implementations
def add_transaction():
    
    transaction_amount = validate_amount() #Made a function for getting the amount input and for validating it. (Line 113)
    
    transaction_category = validate_category() #Made a function for getting the category input and for validating it. (Line 124)

    transaction_type = validate_type() #Made a function for gettint the type and the type input for validating it. (Line 133)

    transaction_date = validate_date() #Made a function for getting the date input and for validatin the date. (Line 141)

    transaction = [transaction_amount, transaction_category, transaction_type, transaction_date]
    transactions.append(transaction) #Appending to the global list
    print("Transaction added Successfully!")
    save_transactions()

def view_transactions():
    if not transactions: #If there are no transactions the below block will be printed.
        print("No transactions found!")
    else: #Else transaction list will be printed with the entered details.
        print("Transactions:")
        for transaction in transactions:
            print(transaction)


def update_transaction():
    # Placeholder for update transaction logic
    # Remember to use save_transactions() after updating
    view_transactions()
    index = int(input("Enter the index of transaction that you need to change : "))
    if 0 < index <= len(transactions):
        transaction_amount = validate_amount() #Line 113
    
        transaction_category = validate_category() #Line 124

        transaction_type = validate_type() #Line 133

        transaction_date = validate_date() #Line 141

        transactions[index-1] = [transaction_amount, transaction_category, transaction_type, transaction_date]
        #Assuming the user doesn't know how python indexing works i substracted 1 from the user's input so the user gets the correct output he asked for.
        print("Transaction Updates Successfully!")
        save_transactions()
    else: 
        print("Transactions not found!")

def delete_transaction():
    # Placeholder for delete transaction logic
    # Remember to use save_transactions() after deleting
    view_transactions()
    index = int(input("Enter the index of transaction : "))
    while True:
        if 0 <= index <= len(transactions):
            del transactions[index-1] #Assuming that the user doesn't know how python indexing works 
            print("Transaction deleted successfully!")
            save_transactions()
            break
        else:
            print("Transaction doesn't exist. Please enter a index greater than 0")
            index = int(input("Enter the index of transaction : "))

def display_summary():
    # Placeholder for summary display logic
    count_transactions = len(transactions) #Getting the length of the transactions list
    print(f'(No. of transactions : {count_transactions})') #Representing the number of transactions by getting the lenght in the above statement
    total_income = 0 #Variable to store the total income
    total_expense = 0 #Variable to store the total expense
    income = 0 #Variable to store the no. of income transactions
    expense = 0 #
    for transaction in transactions:
        if transaction[2] == 'Income':
            total_income += transaction[0] #Add the transaction value to the total income
            income = income + 1 #Add 1 to every income transaction to calculate the total income transactions

    for transaction in transactions:
        if transaction[2] == 'Expense':
            total_expense += transaction[0] #Add the transaction value to the total expense
            expense = expense + 1 #Add 1 to every expense transaction to calculate the total expense transactions

    net_balance = total_income - total_expense #Substracting total expense from total income to get the net balance

    print(f'No. Of Income Transactions: {income}')
    print(f'No. Of Expense Transactions: {expense}')
    print(f'Total Income : {total_income}')
    print(f'Total Expenses : {total_expense}')
    print(f'Net Balance : {net_balance}')


#Functions that i created

def validate_amount():
    while True:
        try:
            transaction_amount = float(input("Enter the Amount : ")) #Declared the amount as a float value coz there can be cents too.
            if transaction_amount <= 0: #Checking whether the input amount is a negative number.
                print("Please enter a value more than 0") #If it is prints this block.
            else:
                return transaction_amount #If not returns the amount
        except ValueError: #If the user didn't input a numeric value for the amount instead a string or something else then a valueError is raised and will print the below block.
            print("Please enter a numeric value")

def validate_category():
    while True:
        transaction_category = input("Enter the Category : ").lower().capitalize() #Category is a string and used .lower() and .capitalize() for styling purposes.
        if transaction_category.isdigit(): #Checking if the transaction category is a numeric value if it is prints the below block.
            print("Category cannot be a numeric value. Please enter a description of the transaction.")
        else: #Else ask for an input again from the user.
            return transaction_category #Then returning the transaction category.

def validate_type():
    while True:
        transaction_type = str(input("Enter the Type : ")).lower().capitalize() #Type is a string and used .lower() to check if the input is a valid response and to compare in the display summary() function. Otherwise the user can input whatever he wants and it will continue. Used .capitalize() for styling purposes.
        if transaction_type == "Income" or transaction_type == "Expense": #Checking if the input is valid
            return transaction_type #If so return transaction type.
        else: #Else print the below block.
            print("Please enter a valid transaction type (Income | Expense)")

def validate_date():
    while True:
        transaction_year = input("Enter the Year (YYYY->2024): ") #Asking for the year
        transaction_month = input("Enter the Month (MM->04): ") #Asking for the month
        transaction_day = input("Enter the Day (DD-04): ") #Asking for the day
        transaction_date = f'{transaction_year}-{transaction_month}-{transaction_day}' #Interpret the year, month and day in the standard format by declaring a varible and using a f string.

        try: 
            datetime.strptime(transaction_date, "%Y-%m-%d") #Using datetime library i am checking if the user entered values are correct coz otherwise user can put 500 to date and month to 20 likewise. I am restricting that using this library.
            return transaction_date #If it's correct return transaction date.
        except ValueError: #If the user input a 500 to a day or 20 to a month a value error will be raised and if that happens the below block will be printed.
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
