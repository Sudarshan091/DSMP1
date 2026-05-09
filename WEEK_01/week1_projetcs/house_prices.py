"""You have a raw list of house prices 🏠 that you need to preprocess:
prices = [150000, 85000, 220000, 90000, 300000]

Write a Python script that does the following:

Creates an empty list called premium_houses.

Uses a loop to check each price in the prices list.

If the price is greater than or equal to 100000, add it to the premium_houses list.

Finally, print the total count of premium houses found."""


prices = [150000, 85000, 220000, 90000, 300000] 
premium_houses=[]
for i in prices:
    if i>=100000:
        premium_houses.append(i)
print(len(premium_houses))
print(premium_houses)


