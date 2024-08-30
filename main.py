import database as db
import income as inc
import expenses as exp
import generate as gen

class Finance:

    def __init__(self):
        try:
            self.db_connection = db.database()
        except Exception as e:
            print(f"Error: {e}")

        self.dic = {1: self.income, 2: self.expenses, 3: self.generate}

        self.user_interaction()

    def user_interaction(self):
        while True:
            try:
                value = int(input("Enter what you want to do (1: Income, 2: Expenses, 3: Generate, 4: Exit): "))
                if value in self.dic:
                    self.dic[value]()
                elif value == 4:
                    print("Database Connection closed")
                    print("Exiting..........")
                    break
                else:
                    print("Wrong input, please try again.")
            except ValueError:
                print("Invalid input! Please enter a number.")

    def income(self):
        inc.income()

    def expenses(self):
        exp.expenses()

    def generate(self):
        gen.generate()


fin = Finance()
