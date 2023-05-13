# BankAccount

class BankAccount:
    def __init__(self):
        self.balance = 0
        self.account_number = ""


    def deposit(self):
        account_number = str(input("Please tell me your account name:\t "))
        print("\nEntered your account number is ", account_number)
        amount_deposit = float(input("Please tell me the amount for deposit: "))
        self.balance += amount_deposit
        print("\n Amount Deposited:", amount_deposit)

    def withdraw(self):
        amount_withdraw = float(input("Please tell me the amount for withdraw: "))
        if self.balance >= amount_withdraw:
            self.balance -= amount_withdraw
            print("\n You Withdrawn:", amount_withdraw)
        else:
            print("\n Insufficient fund  ")

    def display(self):
        print("\n Here is your Available balance =", self.balance)


summary = BankAccount()
summary.deposit()
summary.withdraw()
summary.display()