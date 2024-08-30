import sqlite3
import numpy as np
import matplotlib.pyplot as plt
import datetime

def income_graph(curr):
    amount1 = curr.execute("SELECT AMOUNT FROM INCOME").fetchall()
    date = curr.execute("SELECT DATE FROM INCOME").fetchall()

    amount = np.array([a[0] for a in amount1])
    date = np.array([d[0] for d in date])
    date = np.array([datetime.datetime.strptime(d, "%Y-%m-%d") for d in date])

    plt.plot(date, amount, label='Income', color='green', marker='o')
    plt.xlabel('Date')
    plt.ylabel('Amount')
    plt.title('Income Over Date')
    plt.xticks(rotation=45)  # Rotate date labels for better readability
    plt.tight_layout()  # Adjust layout to prevent clipping of labels
    plt.show()

def expense_graph(curr):
    amount = curr.execute("SELECT AMOUNT FROM EXPENSES").fetchall()
    date = curr.execute("SELECT DATE FROM EXPENSES").fetchall()

    amount = np.array([a[0] for a in amount])
    date = np.array([d[0] for d in date])
    date = np.array([datetime.datetime.strptime(d, "%Y-%m-%d") for d in date])

    plt.plot(date, amount, label='Expenses', color='red', marker='o')
    plt.xlabel('Date')
    plt.ylabel('Amount')
    plt.title('Expenses Over Date')
    plt.xticks(rotation=45)  # Rotate date labels for better readability
    plt.tight_layout()  # Adjust layout to prevent clipping of labels
    plt.show()

def incomeVsExpense(curr):
    # Fetch data from the database
    income_amount = curr.execute("SELECT AMOUNT FROM INCOME").fetchall()
    income_date = curr.execute("SELECT DATE FROM INCOME").fetchall()
    expense_amount = curr.execute("SELECT AMOUNT FROM EXPENSES").fetchall()
    expense_date = curr.execute("SELECT DATE FROM EXPENSES").fetchall()

    income_amount = np.array([a[0] for a in income_amount])
    income_date = np.array([d[0] for d in income_date])
    income_date = np.array([datetime.datetime.strptime(d, "%Y-%m-%d") for d in income_date])

    expense_amount = np.array([a[0] for a in expense_amount])
    expense_date = np.array([d[0] for d in expense_date])
    expense_date = np.array([datetime.datetime.strptime(d, "%Y-%m-%d") for d in expense_date])

    # Calculate the cumulative sum of income
    cumulative_income = np.cumsum(income_amount)
    cumulative_expense = np.cumsum(expense_amount)

    # Plot the data
    plt.figure(figsize=(10, 6))
    plt.plot(income_date, cumulative_income, label="Cumulative Income", color='green', marker='o')
    plt.plot(expense_date, cumulative_expense, label="Cumulative Expenses", color='red', marker='+')

    plt.xlabel('Date')
    plt.ylabel('Amount')
    plt.title('Cumulative Income vs Expenses Over Time')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()  # Adjust layout to prevent clipping of labels
    plt.show()

def generate():
    db = sqlite3.connect("finance.db")
    curr = db.cursor()

    print("Generate, 1) Income 2) Expenses 3) Income vs Expenses")
    gen_value = int(input("Enter : "))

    if gen_value == 1:
        income_graph(curr)
    elif gen_value == 2:
        expense_graph(curr)
    elif gen_value == 3:
        incomeVsExpense(curr)
    else:
        print("Wrong input")

    # Display all records from INCOME and EXPENSES tables
    X = curr.execute("SELECT * FROM INCOME")
    print("Income Table Data:")
    print(X.fetchall())
    Y = curr.execute("SELECT * FROM EXPENSES")
    print("Expenses Table Data:")
    print(Y.fetchall())

generate()
