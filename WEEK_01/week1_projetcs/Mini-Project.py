# Show the user a menu of 3 items with prices.

# Ask the user what they want to order.

# If they pick an item on the menu, add its price to a total_bill variable.

# If they pick something not on the menu, tell them it's unavailable.

# Keep asking them for orders until they type "done".

# Finally, print out their total bill.


# sabse pehle ek banda ek cafee par jaega uske baaad use waha ke available items offer kiye jayenge just like waiter 
# and menu card after that he order some of them that he likes most 
# and then the total bill showed to the user 

# user =input("Enter your name: ")
# cafe_name='Bihar Cafe'
# print(f"Welcome to the {cafe_name} ")
# waiter1="good evening sir"
# print(waiter1)

# item=['cold cofee','hot cofee','momos','burger']
# price=[120,100,60,70]
# menu={i:j for i,j in zip(item,price)}
# print(f'these are some items that is available now{menu}')

# total_bill=0
# order=input("i want  to order:('cold cofee','hot cofee','momos','burger':)")
# while True:
    
#     if order in menu:
#         total_bill+=menu[order]

#         print(f'you have to pay {total_bill}')
#     if order=="done":
#         print(f'your total bill is {total_bill}')
#         break

#     if order not in menu:
#         print("this item is not available currently ")




user = input("Enter your name: ")
cafe_name = 'Bihar Cafe'
print(f"Welcome to {cafe_name}, {user}!")
waiter1 = "Good evening!"
print(waiter1)

# Setting up the menu
item = ['cold cofee', 'hot cofee', 'momos', 'burger','litti chokha','dal bhaat']
price = [120, 100, 60, 70,80,100]
menu = {i: j for i, j in zip(item, price)}
print(f'\nThese are the items available now: {menu}\n')

total_bill = 0

# 1. Start the infinite loop
while True:
    # 2. Ask for the order INSIDE the loop
    order = input("What would you like to order? (type 'done' to finish): ")

    # 3. Check if they want to stop
    if order == 'done':
        print("Finishing your order...")
        break  # This immediately exits the while loop!

    # 4. Check if the item is in the menu
    if order in menu:
        total_bill += menu[order]
        print(f"Added {order}. Current total: {total_bill}")
        
    # 5. Handle items not on the menu
    else:
        print(f"Sorry, we don't have '{order}' right now. Please check the menu.")

# 6. This runs only AFTER the loop is broken
print(f"\nThank you for visiting {cafe_name}! Your final bill is {total_bill}.")

def calculate_total(total_bill,tip_percentage):
    tip_amount= total_bill*(tip_percentage/100)
    print(f'tip amount is {tip_amount}')
    total=total_bill+tip_amount
    return total

tip_percentage=int(input('tip in %'))    
total_bill=calculate_total(total_bill,tip_percentage)

print(f'your total bill is {total_bill}')   