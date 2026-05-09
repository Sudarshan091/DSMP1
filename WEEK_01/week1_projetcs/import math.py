# import math
# num=int(100)
# num2=math.sqrt(num)
# print(num2)

"""
Project Requirements:

Import the random module at the top.

Generate a random number between 1 and 20 and save it in a variable called target.

Set a variable called attempts to 0.

Create a while True: loop to keep asking the user to "Guess a number between 1 and 20: ".

Inside the loop, add 1 to their attempts every time they guess.

Check their guess:

If it's too high, print "Too high! Try again."

If it's too low, print "Too low! Try again."

If they guess correctly, print a victory message that includes how many attempts it took, and break the loop."""
import random 
target=random.randint(1,20)
attempts=0
while True:
    guess=int(input("guess a number between 1 and 20 :"))
    attempts+=1
    if guess>target:

        print('too high , try again')
    elif guess<target:

        print('too low , try again')

    elif guess==target:
        print(f'you win you guessed the correct number{target}')   
        print(f'you took {attempts} attempts')
        break 
