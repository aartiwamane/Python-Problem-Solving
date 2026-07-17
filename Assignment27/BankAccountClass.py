class BankAccount():

    ROI = 10.5

    def __init__(self,AccountName, AccountBalance):
        self.Name = AccountName
        self.Amount = AccountBalance
        
    def Display(self):
        print(f"Account Holder Name is : {self.Name}")
        print(f"Account Holder's Current Balance : {self.Amount}")

    def Deposite(self,Deposite_Amount):
        self.Amount = self.Amount+Deposite_Amount
        return self.Amount

    def Withdraw(self,Withdraw_Amount):
        self.Amount = self.Amount-Withdraw_Amount
        return self.Amount

    def CalculateIntersest(self):
        Interest = (self.Amount * BankAccount.ROI)/100
        return Interest
    
obj1 = BankAccount("AARTI WAMANE", 51000)
obj1.Display()

DepositAmount = int(input(f"Enter the Amount to e Deposited : "))
res1 = obj1.Deposite(DepositAmount)
print(f"Amount after Deposite : {res1}")

WithdrawAmount = int(input(f"Enter the Amount to Winthdraw : "))
res2 = obj1.Withdraw(WithdrawAmount)
print(f"Amount after Withdraw : {res2}")

res3 = obj1.CalculateIntersest()
print(f"Total Interest : {res3}")

obj2 = BankAccount("Amit Patil", 21000)
obj2 .Display()

DepositAmount = int(input(f"Enter the Amount to e Deposited : "))
res1 = obj2.Deposite(DepositAmount)
print(f"Amount after Deposite : {res1}")

WithdrawAmount = int(input(f"Enter the Amount to Winthdraw : "))
res2 = obj2.Withdraw(WithdrawAmount)
print(f"Amount after Deposite : {res2}")

res3 = obj2.CalculateIntersest()
print(f"Total Interest : {res3}")