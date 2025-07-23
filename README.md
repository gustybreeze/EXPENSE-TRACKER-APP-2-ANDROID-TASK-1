# EXPENSE-TRACKER-APP-2-ANDROID-TASK-1













Project Type: Python-based GUI App
Goal: Track expenses, categorize them, and view a pie chart summary.

📌 Description
This is a simple Expense Tracker Application built using Python (Tkinter) and SQLite database. It allows users to:

Add expenses with date, category, amount, and description.

View total expenses by category in a pie chart using matplotlib.

Save data persistently using a local database (expenses.db).

🎯 Features
✔️ Add expense with proper validation

✔️ Categories: Food, Transport, Utilities, Entertainment, Other

✔️ Auto-saved data using SQLite

✔️ Visual Summary using Pie Chart

✔️ Easy-to-use GUI (built with Tkinter)

🧑‍💻 Technologies Used
Component	Tech Used
Language	Python 3
GUI Framework	Tkinter
Database	SQLite
Data Visualization	Matplotlib

🖥️ How to Run
🔹 Requirements:
Make sure Python is installed. Install dependencies (if not already):

bash
Copy
Edit
pip install matplotlib
🔹 Run the App:
bash
Copy
Edit
python expense_tracker.py
📸 Screenshots
Add Expense Form	Pie Chart Summary

📌 You can capture screenshots and save them in a folder called screenshots/ to include them above.

📂 Files & Folders
bash
Copy
Edit
ExpenseTrackerApp/
│
├── expense_tracker.py       # Main application
├── expenses.db              # SQLite database (auto-created)
├── README.md                # Project documentation
├── screenshots/             # Add UI screenshots here (optional)
🧪 Sample Data (In App)
Date	Category	Amount	Description
2025-07-23	Food	150	Lunch with team
2025-07-24	Transport	70	Auto fare

🧹 Future Improvements
Export expenses to CSV or PDF

Add filters (by date or category)

Show total expense and balance

Add login system for multiple users

👨‍💻 Developed by
Sameer Mishra
