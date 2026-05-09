""". Project Requirements:

Define a function called calculate_total.

Give it two parameters: bill_amount and tip_percentage.

Inside the function, calculate the tip amount. (Formula: bill_amount * (tip_percentage / 100))

Calculate the total bill by adding the bill_amount and the tip amount together.

Use the return keyword to send that total back.

Outside the function, call calculate_total(100, 10) (a 100 rupee bill with a 10% tip), save the result in a variable, and print it out."""
total_bill=2000
def calculate_total(total_bill,tip_percentage):
    tip_amount= total_bill*(tip_percentage/100)
    print(f'tip amount is {tip_amount}')
    total=total_bill+tip_amount
    return total

tip_percentage=int(input('tip in %'))    
total_bill=calculate_total(total_bill,tip_percentage)

print(f'your total bill is {total_bill}')   