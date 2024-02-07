class Bank_Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, sumofwithdraw ):
        self.sumofwithdraw = sumofwithdraw
    
    def check_value(self):
        if self.balance < self.sumofwithdraw:
            print("There are not enough balance to withdrawl")



