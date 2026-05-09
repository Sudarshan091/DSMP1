# The ATM Simulator
print('welcome to HDFC Bank ATM')
bank_balance =5000

while True:
    option=input("enter options(1,2,3,4) like \n1 for showing bank balance: \n2 for deposit money in your account: \n3 for withdraw money from your account: \n4 for exit:\n now enter your option:")
    if option=='1':
        print(f'your balance is: {bank_balance}')
    elif option=='2':
        deposit=int(input('enter the deposit amount:'))
        bank_balance+=deposit
        print(f'your balance is {bank_balance}')
    elif option=='3':
        withdraw=int(input('enter the withdraw amount:'))
        if withdraw<=bank_balance:
            bank_balance-=withdraw
            print(f'your balance is {bank_balance}:')
        else:
            print('insufficient balance')
    
    elif option=='4':
        print('thankyou for visisting our bank')
        break
        
    else:
        print('invalid option please try again ')
