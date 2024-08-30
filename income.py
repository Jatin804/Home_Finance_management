
import sqlite3
from datetime import date

def income():
    db = sqlite3.connect("finance.db")
    curr = db.cursor()

    id = int(input("Enter the id of the income: "))
    source = input("Enter the reason for the income: ")
    amount = float(input("Enter the amount of the income: "))
    day = date.today().isoformat()


    curr.execute("INSERT INTO INCOME VALUES (?, ?, ?, ?)", (id, source, amount, day))
    db.commit()
    print("Your inputs are saved successfully..")

    # print(curr.execute("SELECT * FROM INCOME").fetchall())
