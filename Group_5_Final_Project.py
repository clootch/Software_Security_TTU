import threading
import sys
import hashlib
import sqlite3


class Customer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.connection = sqlite3.connect("Customer_Teller_loginInfo.db")
        self.cursor = self.connection.cursor()

    def log_on(self):
        # assume user info is already in the data base
        userId = input(str("ID: "))
        userPass = input(str("Password: "))

        # grants access if hashed password matches the data base
        cursor.execute("SELECT * FROM users WHERE userId = ?", (userId,))
        user = cursor.fetchall()
        try:
            if user[0][1] != hashlib.sha256(userPass.encode()).hexdigest():
                print("Password did not match.")
                print()
                return
        except:
            print("That username does not exist.")
            return

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

            choice = input("Enter a number choice here: ")
            if choice == "1":
                # return to menu
                pass
            if choice == "2":
                self.query_account(userId)
            if choice == "3":
                self.transfer_funds(userId)
            if choice == "4":
                self.view_profile(userId)
            if choice == "5":
                self.query_stock(userId)
            if choice == "6":
                self.buy_stock(userId)
            if choice == "7":
                confirm = self.log_out()
                if confirm:
                    return
                else:
                    pass

    def log_out(self):
        choice = input("Are you sure you want to log-off?\nEnter y for yes, anything else for no: ")
        if choice == 'y':
            return True
        else:
            return False

    def query_account(self, userId):
        print()
        acc_num = input("Enter the account number: ")

        # input logic here for checking account number with user
        cursor.execute("SELECT * FROM users WHERE AccountNumber = ?", (acc_num,))
        accInfo = cursor.fetchone()

        if userId == accInfo[0]:
            print("Valid account number\n")
            cursor.execute("SELECT * FROM Bank_Account where UserId = ?", (userId,))
            balanceInfo = cursor.fetchone()
            print("Your account balance: $", balanceInfo[1])
        else:
            print("Invalid account number")
            return

    def transfer_funds(self, userId):
        print("\nTransfer funds\n\n\n")
        transferAmount = float(input("Enter amount: $"))
        fromAccount = int(input("Enter your account number: "))
        toAccount = int(input("Enter the account number of the receiver: "))

        cursor.execute("SELECT * FROM users WHERE userId = ?", (userId,))
        accInfo = cursor.fetchone()

        # checks if fromAccount matches their account number
        if str(fromAccount) == str(accInfo[2]):

            # checks if toAccount number exists
            cursor.execute("SELECT * From users WHERE AccountNumber = ?", (toAccount,))
            accnumberInfo = cursor.fetchall()
            if len(accnumberInfo) != 0:

                # check sending amount
                cursor.execute("SELECT * FROM Bank_Account WHERE UserId = ?", (userId,))
                bankInfo = cursor.fetchone()
                if transferAmount <= bankInfo[1]:

                    # create a message digest to make sure transfer account has not been tampered
                    amountHash = hashlib.sha256(str(transferAmount).encode()).hexdigest()
                    print("Sending $", transferAmount, "to account number:", toAccount)

                    # update user bank account balance
                    newAmount = bankInfo[1] - transferAmount
                    print(newAmount)
                    cursor.execute("UPDATE Bank_Account SET Balance = ? WHERE userId = ?", (newAmount, userId))
                    cursor.execute("SELECT * FROM Bank_Account WHERE UserId = ?", (userId,))
                    dx = cursor.fetchone()
                    connection.commit()
                else:
                    print("Insufficient balance")
                    return
            else:
                print("Invalid sending account number")
                return
        else:
            print("Invalid account number")
            return

    def view_profile(self, userId):
        cursor.execute("SELECT * FROM User_Profile WHERE userId = ?", (userId,))
        userProfile = cursor.fetchone()
        print("User profile\n")
        print("userId: ", userId)
        print("\nFull Name: ", userProfile[1])
        print("\nSSN: ", userProfile[2])
        print("\nAddress: ", userProfile[3])
        print("\nPhone number: ", userProfile[4])
        print("\nIncome: $", userProfile[5])
        print("\nEmail: ", userProfile[6])

    def query_stock(self, userId):
        cursor.execute("SELECT * FROM Stock_Transactions WHERE userId = ?", (userId,))
        userStockInfo = cursor.fetchall()

        if len(userStockInfo) == 0:
            print("This user has no stock information at this time")
        else:
            pass


    def buy_stock(self, userId):
        cursor.execute("SELECT * FROM Bank_Account WHERE UserId = ?", (userId,))
        bankInfo = cursor.fetchone()
        print("User balance: $", bankInfo[1])
        print("\n")
        stock_name = str(input("Enter stock name: "))
        stock_quantiy = int(input("Enter stock quantity: "))
        stock_unit_price = int(input("Enter stock price: "))
        acc_num = int(input("Enter account number: "))

        total_stock_price = stock_quantiy * stock_unit_price
        userBalance = bankInfo[1]
        if total_stock_price <= userBalance:
            stock_contract = stock_name + str(stock_quantiy) + str(stock_unit_price) + str(acc_num) + "B"
            print(stock_contract)
            # create digital signature of the
        else:
            print("Insufficient fund")
            quit(0)





    def sell_stock(self):
        pass


class Bank_Teller(threading.Thread):
    def __init__(self):
        pass

    def log_on(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        cursor.execute("SELECT * FROM users WHERE userId = ?", (username,))
        user = cursor.fetchall()
        try:
            if user[0][1] != hashlib.sha256(password.encode()).hexdigest():
                print("Password did not match.")
                print()
                return
        except:
            print("That username does not exist.")
            return
        # input logic here to confirm user/pass
        while True:
            print("----------------------------------")
            print(" What would you like to do?")
            print(" 1. Log Off")
            print(" 2. Query Account")
            print(" 3. Withdraw Funds")
            print(" 4. View Profile")
            print(" 5. Query Stock")
            print("----------------------------------")
            choice = input("Enter a number choice here: ")
            if choice == "1":
                confirm = self.log_out()
                if confirm:
                    return
            if choice == "2":
                self.query_account()
            if choice == "3":
                self.withdraw_funds()
            if choice == "4":
                self.view_profile()
            if choice == "5":
                self.query_stock()

    def log_out(self):
        choice = input("Are you sure you want to log-off?\nEnter y for yes, anything else for no: ")
        if choice == 'y':
            return True
        else:
            return False

    def query_account(self):
        print()
        acc_num = input("Enter the account number: ")
        print(acc_num)
        cursor.execute("SELECT * FROM users WHERE AccountNumber = ?", acc_num)
        info = cursor.fetchall()
        if len(info) == 0:
            print("That account number was invalid.")
            return
        cursor.execute("SELECT * FROM Bank_Account WHERE userId = ?", (info[0][0],))
        print("Remaining Balance: $" + str(cursor.fetchall()[0][1]))
        print()

    def withdraw_funds(self):
        print()
        amount = input("How much would you like to withdrawl: ")
        accnum = input("Which account are you pulling from: ")
        cursor.execute("SELECT * FROM users WHERE AccountNumber = ?", accnum)
        userInfo = cursor.fetchall()
        try:
            userInfo = userInfo[0]
        except:
            print("Could not find a user with that account number.")
            return
        cursor.execute("SELECT * FROM Bank_Account WHERE userId = ?", (userInfo[0],))
        balance = cursor.fetchall()[0][1]
        if balance >= int(amount):
            # good to go
            balance -= int(amount)
            a = input("Did you give the customer their cash? Enter Y to continue")
            if a == "y":
                cursor.execute("UPDATE Bank_Account SET Balance = ? WHERE userId = ?", (balance, userInfo[0]))
            else:
                print("")
                return
        else:
            print("The balance was less than the amount asked.")
            return
        print()

    def view_profile(self):
        print()
        name = input("What is the customer's name: ")
        ssn = input("What is the customers ssn: ")
        cursor.execute("SELECT * FROM User_Profile WHERE name = ? AND ssn = ?", (name, ssn))
        try:
            stuff = cursor.fetchall()[0]
        except:
            print("Could not find a user with those credientals.")
            return
        print("""
UserId: {}
Name: {}
SSN: {}
Address: {}
Phone Number: {}
Income: {} 
Email: {}
        """.format(stuff[0], stuff[1], stuff[2], stuff[3], stuff[4], stuff[5], stuff[6]))
        print()

    def query_stock(self):
        print()
        name = input("What is the customer's name: ")
        cursor.execute("SELECT * FROM User_Profile WHERE name = ?", (name,))
        try:
            userId = cursor.fetchall()[0][0]
        except:
            print("User not found.")
            return
        cursor.execute("SELECT * FROM Stock_Transactions WHERE userId = ?", (userId,))
        try:
            for stuff in cursor.fetchall():
                print("""
Stock Name: {}
Type: {}
Amount: {}
Unit Price: {}
                """.format(stuff[1], stuff[2], stuff[3], stuff[4]))
        except:
            print("There are no transactions on this account.")
        print()


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
