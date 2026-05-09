#in this program we are going to find the maximum of three number given by the user 
 
a = int(input('enter first number '))
b = int(input('enter second number '))
c = int(input('enter third number '))       

if a > b and a > c:
    print(f'{a} is maximum')
elif b > a and b > c:
    print(f'{b} is maximum')
else:
    print(f"{c} is maximum")    
    