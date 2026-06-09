class Account:
     def __init__(self,bal,acc):
         self.balance = bal
         self.account_no = acc

     def debit(self,ammount):
         self.balance -= ammount
         print("TK.",ammount,"was debited")
         print("total balance:",self.get_balance())
     def get_balance(self):
         return self.balance
acc1 = Account(10000,12345)
acc1.debit(10000)
print(acc1.balance)
print(acc1.account_no)