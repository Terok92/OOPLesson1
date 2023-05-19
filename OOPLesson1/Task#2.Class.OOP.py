# BankAccount

class BankAccount:
    def __init__(self):
        self.balance = 0
        self.account_number = ""


    def deposit(self):
        print("\nEntered your account number is ", account_number)
        self.balance += amount_deposit
        print("\n Amount Deposited:", amount_deposit)

    def withdraw(self):
        if self.balance >= amount_withdraw:
            self.balance -= amount_withdraw
            print("\n You Withdrawn:", amount_withdraw)
        else:
            print("\n Insufficient fund  ")

    def display(self):
        print("\n Here is your Available balance =", self.balance)


account_number = str(input("Please tell me your account name:\t "))
amount_deposit = float(input("Please tell me the amount for deposit: "))
amount_withdraw = float(input("Please tell me the amount for withdraw: "))
summary = BankAccount()
summary.deposit()
summary.withdraw()
summary.display()