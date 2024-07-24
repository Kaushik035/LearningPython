class Account:
    def __init__(self,balance,account_no):
        self.balance = balance
        self.account_no = account_no

    def debit(self,amount):
        self.balance = self.balance - amount
        return self.balance