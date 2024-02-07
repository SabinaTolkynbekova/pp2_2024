class Bank_Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount>0:
            self.balance += amount
            print(f"Deposit of ${amount} accepted. New balance: ${self.balance}")
        else:
            print("Deposit amount must be greater than zero.")
    
    def withdraw(self, amount):
        if amount>0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrawl of ${amount} accepted. New balance: ${self.balance}")
            else:
                print("Insufficient funds!! Withdrawal denied.")
        else:
            print("Withdrawal must be greater than zero.")

name = input()
first_balance = int(input())
account = Bank_Account(name, first_balance)
while True:
    print("\n1. Deposit\n2. Withdraw\n3. Exit")
    choice = input("enter your choice (1/2/3): ")

    if choice == '1':
        amount = float(input("Enter deposit amount: "))
        account.deposit(amount)

    elif choice == '2':
        amount = float(input("Enter withdrawal amount: "))
        account.withdraw(amount)

    elif choice == '3':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. You can enter 1,2 or 3.")