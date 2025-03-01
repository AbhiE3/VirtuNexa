import datetime
import json
import tkinter as tk
from tkinter import messagebox

class FinanceTracker:
    def __init__(self, data_file='transactions.json'):
        self.data_file = data_file
        self.transactions = self.load_transactions()

    def load_transactions(self):
        """Load transactions from a JSON file."""
        try:
            with open(self.data_file, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_transactions(self):
        """Save transactions to a JSON file."""
        with open(self.data_file, 'w') as file:
            json.dump(self.transactions, file, indent=4)

    def add_transaction(self, amount, category, transaction_type):
        """Add an income or expense transaction."""
        transaction = {
            'date': datetime.date.today().isoformat(),
            'amount': amount,
            'category': category,
            'type': transaction_type
        }
        self.transactions.append(transaction)
        self.save_transactions()
        messagebox.showinfo("Success", "Transaction added successfully.")

    def generate_report(self):
        """Generate a monthly financial summary."""
        income = sum(t['amount'] for t in self.transactions if t['type'] == 'income')
        expenses = sum(t['amount'] for t in self.transactions if t['type'] == 'expense')
        balance = income - expenses
        
        report = f"Total Income: ${income:.2f}\nTotal Expenses: ${expenses:.2f}\nBalance: ${balance:.2f}"
        messagebox.showinfo("Monthly Report", report)

class FinanceApp:
    def __init__(self, root):
        self.tracker = FinanceTracker()
        self.root = root
        self.root.title("Personal Finance Tracker")
        
        # Amount Entry
        tk.Label(root, text="Amount:").grid(row=0, column=0)
        self.amount_entry = tk.Entry(root)
        self.amount_entry.grid(row=0, column=1)
        
        # Category Entry
        tk.Label(root, text="Category:").grid(row=1, column=0)
        self.category_entry = tk.Entry(root)
        self.category_entry.grid(row=1, column=1)
        
        # Buttons
        tk.Button(root, text="Add Income", command=self.add_income).grid(row=2, column=0)
        tk.Button(root, text="Add Expense", command=self.add_expense).grid(row=2, column=1)
        tk.Button(root, text="Generate Report", command=self.tracker.generate_report).grid(row=3, column=0, columnspan=2)
        tk.Button(root, text="Exit", command=root.quit).grid(row=4, column=0, columnspan=2)
    
    def add_income(self):
        self.add_transaction("income")
    
    def add_expense(self):
        self.add_transaction("expense")
    
    def add_transaction(self, transaction_type):
        try:
            amount = float(self.amount_entry.get())
            category = self.category_entry.get()
            if not category:
                raise ValueError("Category cannot be empty.")
            self.tracker.add_transaction(amount, category, transaction_type)
        except ValueError as e:
            messagebox.showerror("Error", f"Invalid input: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = FinanceApp(root)
    root.mainloop()
