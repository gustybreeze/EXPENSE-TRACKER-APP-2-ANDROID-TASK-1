import sqlite3
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk, messagebox


# database setup
conn = sqlite3.connect('expenses.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        category TEXT,
        amount REAL,
        description TEXT
    )
''')
conn.commit()


# functions
def add_expense():
    date = entry_date.get()
    category = combo_category.get()
    amount = entry_amount.get()
    description = entry_description.get()

    if date and category and amount:
        try:
            cursor.execute("INSERT INTO expenses (date, category, amount, description) VALUES (?, ?, ?, ?)",
                           (date, category, float(amount), description))
            conn.commit()
            messagebox.showinfo("Success", "Expense added successfully!")
            entry_date.delete(0, tk.END)
            entry_amount.delete(0, tk.END)
            entry_description.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount.")
    else:
        messagebox.showerror("Error", "All fields are required!")

def show_summary():
    cursor.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
    data = cursor.fetchall()
    if data:
        categories, amounts = zip(*data)
        plt.figure(figsize=(6,6))
        plt.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=140)
        plt.title("Expense Summary by Category")
        plt.axis('equal')
        plt.show()
    else:
        messagebox.showinfo("No Data", "No expenses found!")


# UI setup
root = tk.Tk()
root.title("Expense Tracker")
root.geometry("400x350")

tk.Label(root, text="Date (YYYY-MM-DD):").pack()
entry_date = tk.Entry(root)
entry_date.pack()

tk.Label(root, text="Category:").pack()
combo_category = ttk.Combobox(root, values=["Food", "Transport", "Utilities", "Entertainment", "Other"])
combo_category.pack()

tk.Label(root, text="Amount:").pack()
entry_amount = tk.Entry(root)
entry_amount.pack()

tk.Label(root, text="Description:").pack()
entry_description = tk.Entry(root)
entry_description.pack()

tk.Button(root, text="Add Expense", command=add_expense).pack(pady=10)
tk.Button(root, text="Show Summary", command=show_summary).pack(pady=5)

root.mainloop()


# Close DB on exit
conn.close()
