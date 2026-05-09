"""Smart Calculator (Not a Toy)

Supports +, −, ×, ÷

Handles invalid input

Loop until user exits

Uses functions for each operation

Skills used: loops, conditionals, functions

Challenge yourself: Don’t use eval()."""
# print("welcome to smart calculator ")
# print("give your inputs to the calculator!")
# num1= float(input("enter your first number : "))
# num2= float(input("enter your second numner: "))

# operation= input("+,-,*,/")

# if operation == "+":
#     def add(num1,num2):
#         return num1+num2
#     print(add(num1,num2))

# elif operation == "-":
#     def sub(num1,num2):
#         return num1-num2
#     print(sub(num1,num2))

# elif operation =="*":
#     def mul(num,num2):
#         return num1*num2
#     print(mul(num1,num2))
# elif operation == "/":
#     def div(num1,num2):
#         return num1/num2
#     print(div(num1,num2))   
# else:
#     print("invalid syntax")                 



#upgrade this upper code 

def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def mul(num1,num2):
    return num1*num2
def div(num1,num2):
    if num2 == 0:
        return "error: division by zero"    
    return num1/num2
def power(num1,num2):
    return num1**num2   
def modulo(num1,num2):
    if num2 == 0:
        return "error: division by zero "
    return num1%num2     

print("welcome to smart calculator ")

while True:
    operation = input("enter the operaton (+,-,*,/,**,%) or q to quit: ")
    if operation == "q":
        print("calculator closed")
        break

    if operation not in ("+","-","*","/","**","%"):
        print("invalid operation")
        continue

    num1 = float(input("enter the first number: ".upper()))
    num2 = float(input("enter the second number: ".upper()))
    
    if operation == "+":
        print("result =", add(num1,num2))
    elif operation == "-":
        print("result =", sub(num1,num2))    
    elif operation == "*":
        print("result =", mul(num1,num2))
    elif operation == "/":
        print("result =", div(num1,num2))    
    elif operation == "**":
        print("result =", power(num1,num2))    
    elif operation == "%":
        print("result =", modulo(num1,num2))    
    

        
# Write code here
operations= input("1,2,3,4")
cm=int(input("enter value in cm:"))
km=int(input("enter the kilometer :"))
usd=int(input("enter the money in usd:"))

if operations=="1":
    # cm to ft 
    cm=int(input("enter value in cm:"))
    cm_ft=cm*0.0328084
    print("coverted value of cm in ft=",cm_ft)
elif operations=="2":
    # km to miles 
    km=int(input("enter the kilometer :"))
    km_miles=km*0.621371
    print("converted value of km into miles=",km_miles)
elif operations=="3":
    # usd to inr
    usd=int(input("enter the money in usd:"))
    usd_inr= usd*91.85
    print("converted usd into INR",usd_inr)
