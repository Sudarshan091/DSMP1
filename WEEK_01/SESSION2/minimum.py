# in this program we are going to find the minimum num in a three given number 

a=int(input('enter first number '))
b=int(input('enter second number '))
c=int(input('enter third number '))

if a<b and a<c:
    print(f'{a} is minimum')
elif b<a and b<c:
    print(f'{b} is minimum')
else:
    print(f'{c} is minimum')



