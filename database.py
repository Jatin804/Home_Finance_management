import os
import sqlite3


def database():
    db_name = "finance.db"
    db_exists = os.path.exists(db_name)
    db = sqlite3.connect(db_name)
    curr = db.cursor()

    if not db_exists:
        # Create the tables if the database didn't exist
        curr.execute("""
        CREATE TABLE IF NOT EXISTS INCOME
        (ID INTEGER PRIMARY KEY AUTOINCREMENT,
        SOURCE TEXT NOT NULL,
        AMOUNT REAL NOT NULL,
        DATE INT NOT NULL);""")

        curr.execute("""
        CREATE TABLE IF NOT EXISTS EXPENSES 
        (ID INTEGER PRIMARY KEY AUTOINCREMENT,
        REASON TEXT NOT NULL,
        AMOUNT REAL NOT NULL,
        DATE INT NOT NULL);""")

        db.commit()
        print("Database created successfully")
    else:
        # Check if the necessary tables exist
        curr.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='INCOME';")
        income_table_exists = curr.fetchone()

        curr.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='EXPENSES';")
        expenses_table_exists = curr.fetchone()

        if not income_table_exists or not expenses_table_exists:
            # Create missing tables
            if not income_table_exists:
                curr.execute("""
                CREATE TABLE IF NOT EXISTS INCOME
                (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                SOURCE TEXT NOT NULL,
                AMOUNT REAL NOT NULL,
                DATE TEXT NOT NULL);""")

            if not expenses_table_exists:
                curr.execute("""
                CREATE TABLE IF NOT EXISTS EXPENSES 
                (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                REASON TEXT NOT NULL,
                AMOUNT REAL NOT NULL,
                DATE TEXT NOT NULL);""")

            db.commit()
            print("Tables created successfully in the existing database")
        else:
            print("Connected to the existing database with all required tables.")

    return db

