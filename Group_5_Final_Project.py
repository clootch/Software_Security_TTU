import threading
import sys

class Customer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    
    def run(self):
        while True:
            print("----------------------------------")
            print("What would you like to do?")
            print("1. Return to menu")
            print("----------------------------------")
            choice = input("Enter a number choice here")
            if choice == "1":
                return

    def log_on(self):
        # enters id and pass
        # which are encrypted
        # checks if id and pass is correct, display message based on whether it was succesful login or not
        userId = input(str("ID: "))
        userPass = input(str("Password: "))
        # probably store customer information on sql

        pass

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
        pass

    def log_out(self):
        pass

    def query_account(self):
        pass

    def withdraw_funds(self):
        pass

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
            user.start()
            
        
        elif (choice == "2"):
            print("Bank Teller Login")
        elif (choice == "3"):
            print("Register Account")
        elif (choice == "4"):
            print("Closing system...")
            quit(0)
        else:
            print("Incorrect option...")