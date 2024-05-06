import os
import json
from datetime import datetime

# File paths
DATA_FILE = "finances.json"

# Function to load data from file
def load_data():
    if not os.path.exists(DATA_FILE):
        return {"income": [], "expenses": []}
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except (IOError, json.JSONDecodeError) as e:
        print("Error loading data:", e)
        return {"income": [], "expenses": []}

# Function to save data to file
def save_data(data):
    try:
        with open(DATA_FILE, "w") as file:
            json.dump(data, file, indent=4)
    except IOError as e:
        print("Error saving data:", e)

# Function to add income
def add_income(description, amount):
    try:
        amount = float(amount)
        if amount <= 0:
            print("Amount must be a positive number.")
            return
    except ValueError:
        print("Invalid amount. Please enter a valid number.")
        return
    data = load_data()
    data["income"].append({"description": description, "amount": amount, "date": str(datetime.now())})
    save_data(data)
    print("Income added successfully.")

# Function to add expense
def add_expense(description, amount):
    try:
        amount = float(amount)
        if amount <= 0:
            print("Amount must be a positive number.")
            return
    except ValueError:
        print("Invalid amount. Please enter a valid number.")
        return
    data = load_data()
    data["expenses"].append({"description": description, "amount": amount, "date": str(datetime.now())})
    save_data(data)
    print("Expense added successfully.")

# Function to view summary
def view_summary():
    data = load_data()
    total_income = sum(transaction["amount"] for transaction in data["income"])
    total_expenses = sum(transaction["amount"] for transaction in data["expenses"])
    savings = total_income - total_expenses
    print("Total Income:", total_income)
    print("Total Expenses:", total_expenses)
    print("Savings:", savings)

# Function to view transactions
def view_transactions():
    data = load_data()
    print("Income Transactions:")
    for transaction in data["income"]:
        print(transaction["date"], "-", transaction["description"], "-", transaction["amount"])
    print("\nExpense Transactions:")
    for transaction in data["expenses"]:
        print(transaction["date"], "-", transaction["description"], "-", transaction["amount"])

# Main function
def main():
    print("Personal Finance Manager")
    while True:
        print("\nMenu:")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Summary")
        print("4. View Transactions")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            description = input("Enter description for income: ")
            amount = input("Enter amount for income: ")
            add_income(description, amount)
        elif choice == "2":
            description = input("Enter description for expense: ")
            amount = input("Enter amount for expense: ")
            add_expense(description, amount)
        elif choice == "3":
            view_summary()
        elif choice == "4":
            view_transactions()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
