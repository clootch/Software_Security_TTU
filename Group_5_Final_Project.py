import threading
import sys
import hashlib
import sqlite3


class Customer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.connection = sqlite3.connect("Customer_Teller_loginInfo.db")
        self.cursor = self.connection.cursor()

    def run(self):
        while True:
            print("----------------------------------")
            print("What would you like to do?")
            print("1. Return to menu")
            print("2. Query account")
            print("3. Transfer funds")
            print("4. View profile")
            print("5. Query stock")
            print("6. Buy stock")
            print("7. Log off")
            print("----------------------------------")
            choice = input("Enter a number choice here")
            if choice == "7":
                confirm = self.log_out()
                if confirm:
                    return
                else:
                    pass

    def log_on(self):
        # assume user info is already in the data base
        userId = input(str("ID: "))
        userPass = input(str("Password: "))
        passHash = hashlib.sha256(userPass.encode()).hexdigest()

        # grants access if hashed password matches the data base
        self.cursor.execute("SELECT userPass FROM users WHERE userId = ?", (userId,))
        userPassCheck = self.cursor.fetchone()

        if userPassCheck[0] == passHash:
            print("Password match")
            self.run()
        else:
            print("Username or password does not match")


    def log_out(self):
        pass

    def query_account(self):
        pass

    def transfer_funds(self):
        pass

    def view_profile(self):
        pass

    def query_stock(self):
        pass

    def buy_stock(self):
        pass

    def sell_stock(self):
        pass


class Bank_Teller(threading.Thread):
    def __init__(self):
        pass

    def log_on(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        # input logic here to confirm user/pass
        while True:
            print("----------------------------------")
            print(" What would you like to do?")
            print(" 1. Log Off")
            print("----------------------------------")
            choice = input("Enter a number choice here: ")
            if choice == "1":
                confirm = self.log_out()
                if confirm:
                    return
            if choice == "2":
                self.query_account()

    def log_out(self):
        choice = input("Are you sure you want to log-off?\nEnter y for yes, anything else for no: ")
        if choice == 'y':
            return True
        else:
            return False

    def query_account(self):
        print()
        acc_num = input("Enter the account number: ")
        # input logic here for checking account number
        if acc_num:
            print("Account Balance: 1")
        else:
            print("Accoun Number Invalid, returning to menu...")
        print()

    def withdraw_funds(self):
        print()
        amount = input("How much would you like to withdrawl: ")

        print()

    def view_profile(self):
        pass

    def query_stock(self):
        pass


class Stock_Trading_System(threading.Thread):
    def __init__(self):
        pass

    def buy_stock(self):
        pass

    def sell_stock(self):
        pass


if __name__ == "__main__":
    # user: tellerTest
    # pass: password123 / ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f

    # user: regUserTest
    # pass: password123 / ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f

    # this is a test to see the content of the database
    # I will delete this later
    connection = sqlite3.connect("Customer_Teller_loginInfo.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users")
    print(cursor.fetchall())
    print(type(cursor.fetchall()))


    while True:
        print("----------------------------------")
        print("What would you like to do?")
        print("1. Login as Customer")
        print("2. login as Bank Teller")
        print("3. Register Account")
        print("4. Quit")
        print("----------------------------------")
        choice = input("Enter a number choice here: ")
        if (choice == "1"):
            print("Customer Login")
            user = Customer()
            user.log_on()
            user.start()


        elif (choice == "2"):
            print("Bank Teller Login")
            user = Bank_Teller()
            user.log_on()
        elif (choice == "3"):
            print("Register Account")
        elif (choice == "4"):
            print("Closing system...")
            quit(0)
        else:
            print("Incorrect option...")
