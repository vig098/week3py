import os
import datetime
import json

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.categories = set()
        self.load_data()

    def load_data(self):
        if os.path.exists('expenses.json'):
            with open('expenses.json', 'r') as file:
                data = json.load(file)
                self.expenses = data['expenses']
                self.categories = set(data['categories'])

    def save_data(self):
        data = {
            'expenses': self.expenses,
            'categories': list(self.categories)
        }
        with open('expenses.json', 'w') as file:
            json.dump(data, file)

    def add_expense(self, amount, description, category):
        expense = {
            'date': datetime.date.today().isoformat(),
            'amount': amount,
            'description': description,
            'category': category
        }
        self.expenses.append(expense)
        self.categories.add(category)
        self.save_data()

    def view_expenses(self):
        print("All Expenses:")
        for expense in self.expenses:
            print(f"Date: {expense['date']}, Amount: {expense['amount']}, Description: {expense['description']}, Category: {expense['category']}")

    def view_summary(self):
        monthly_expenses = {}
        for expense in self.expenses:
            date = datetime.datetime.strptime(expense['date'], '%Y-%m-%d').date()
            if date.month == datetime.date.today().month:
                if expense['category'] in monthly_expenses:
                    monthly_expenses[expense['category']] += expense['amount']
                else:
                    monthly_expenses[expense['category']] = expense['amount']
        print("Monthly Expenses Summary:")
        for category, amount in monthly_expenses.items():
            print(f"Category: {category}, Amount: {amount}")

    def run(self):
        while True:
            print("\n1. Add Expense")
            print("2. View Expenses")
            print("3. View Summary")
            print("4. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                amount = float(input("Enter amount: "))
                description = input("Enter description: ")
                category = input("Enter category: ")
                self.add_expense(amount, description, category)
            elif choice == '2':
                self.view_expenses()
            elif choice == '3':
                self.view_summary()
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    tracker = ExpenseTracker()
    tracker.run()