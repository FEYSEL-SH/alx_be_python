class BankAccount:
    def __init__(self, initial_balance=0):
        self.__account_balance = initial_balance 

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposited {amount}. New balance: {self.__account_balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__account_balance}")
            return True
        else:
            print("Insufficient funds or invalid amount.")
            return False

    def display_balance(self):
        print(f"Current balance: {self.__account_balance}")
