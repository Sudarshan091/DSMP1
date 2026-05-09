#Create a function that takes two numbers and returns their sum.
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)
print(result)

#Write a function that checks whether a number is even or odd.
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(check_even_odd(10))

#Create a function that returns the largest among three numbers.
def find_max(a, b, c):
    return max(a, b, c)

print(find_max(4, 9, 2))


#Write a function that calculates factorial of a number.
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(5))

#Write a function to check whether a string is palindrome.
def is_palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

print(is_palindrome("madam"))

#problems 6.  Create a function that counts vowels in a string.
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0

    for char in text:
        if char in vowels:
            count += 1

    return count

print(count_vowels("Artificial Intelligence"))

#problem 7. Write a function to reverse a string.
def reverse_string(s):
    return s[::-1]

print(reverse_string("Python"))
