
import sqlite3
from datetime import date

def expenses():
    id = int(input("Enter the od for the expenses : "))
    reason = input("Enter the reason for the expenses : ")
    amount = int(input("Enter the amount : "))
    day = date.today()

    db = sqlite3.connect("finance.db")
    curr = db.cursor()

    curr.execute("INSERT INTO EXPENSES VALUES (?, ?, ?, ?)", (id, reason, amount, day))
    db.commit()
    print("Expenses data added successfully.. ")

    # data = curr.execute("SELECT * FROM EXPENSES")
    # print(data.fetchall())
