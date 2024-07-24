class Account:
    def __init__(self,balance,account_no):
        self.balance = balance
        self.account_no = account_no

    def debit(self,amount):
        self.balance = self.balance - amount
        print(f"Rupees {amount} is debited from the account",'\n',f"Available balence is rupees {self.balance}")
    
    def credit(self,amount):
        self.balance = self.balance + amount
        print(f"Rupees {amount} is credited to the account",'\n',f"Available balence is rupees {self.balance}")

    def get_balance(self):
        print(f"available balance is {self.balance}")

acc = Account(10000,422)
acc.get_balance()
acc.debit(5000)
acc.credit(2000)

acc.get_balance()
