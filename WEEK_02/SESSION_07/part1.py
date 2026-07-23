# # write your code here
# class BankAccount:
    
#     def __init__(self,accountNumber,Name,Balance):
#         self.accountNumber=accountNumber
#         self.Name=Name
#         self.Balance=Balance
    
#     def display(self):
#         print(f'account number: {self.accountNumber}')
#         print(f'account name: {self.Name}')
#         print(f'account balance: {self.Balance}')

#     def Deposit(self,amount):
#         self.Balance +=amount

#     def Withdrawl(self,amount):
#         if amount > self.Balance:
#             print('insufficient balance')

#         else:
#             self.Balance-=amount
#             reduction=self.bankFees()
#             self.Balance-=reduction

#     def bankFees(self):
#         return 0.5 * self.Balance

# cust=BankAccount(7610396681,'sudarshan',1000)
# cust.Deposit(500)
# cust.Withdrawl(300)
# cust.display()

def Factorial(self, n):
        fact=1
        for i in range(1,n):
            fact*=i
        return fact
note=Factorial(10)       
