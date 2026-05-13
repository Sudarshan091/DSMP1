# Task 6 - Complete Solutions with Explanations

## Problem 1: Remove Duplicates from List

**Problem Statement:**
Write a Python function that takes a list and returns a new list with unique elements of the first list.

**Input:** `[1,2,3,3,3,3,4,5]`  
**Output:** `[1, 2, 3, 4, 5]`

### Solution

```python
def get_unique_elements(lst):
    """Returns a new list with unique elements from the input list."""
    return list(set(lst))

# Test
input1 = [1,2,3,3,3,3,4,5]
output = get_unique_elements(input1)
print(output)  # [1, 2, 3, 4, 5]
```

**Explanation:**
- Convert the list to a `set` which automatically removes duplicates
- Convert back to a list to maintain list data type
- Sets are unordered, so the order might change
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

---

## Problem 2: Sort Hyphen-Separated Words

**Problem Statement:**
Write a Python function that accepts a hyphen-separated sequence of words as parameter and returns the words in a hyphen-separated sequence after sorting them alphabetically.

**Input:** `green-red-yellow-black-white`  
**Output:** `black-green-red-white-yellow`

### Solution

```python
def sort_hyphenated(sequence):
    """Sorts hyphen-separated words alphabetically."""
    words = sequence.split('-')
    words.sort()
    return '-'.join(words)

# Test
input_str = "green-red-yellow-black-white"
result = sort_hyphenated(input_str)
print(result)  # black-green-red-white-yellow
```

**Explanation:**
1. `split('-')` - Splits the string by hyphen delimiter into individual words
2. `sort()` - Sorts the words list in alphabetical order (in-place)
3. `'-'.join(words)` - Joins sorted words back with hyphen separator
- **Time Complexity:** O(n log n) where n is number of words
- **Space Complexity:** O(n)

---

## Problem 3: Count Upper and Lower Case Letters

**Problem Statement:**
Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

**Input:** `'CampusX is an Online Mentorship Program fOr EnginEering studentS.'`  
**Output:**
```
No. of Upper case characters: 9
No. of Lower case characters: 47
```

### Solution

```python
def count_case_letters(string):
    """Counts uppercase and lowercase letters in a string."""
    upper_count = sum(1 for char in string if char.isupper())
    lower_count = sum(1 for char in string if char.islower())
    return upper_count, lower_count

# Test
sample_string = 'CampusX is an Online Mentorship Program fOr EnginEering studentS.'
upper, lower = count_case_letters(sample_string)
print(f"No. of Upper case characters: {upper}")
print(f"No. of Lower case characters: {lower}")
```

**Explanation:**
- `char.isupper()` - Returns True if character is uppercase
- `char.islower()` - Returns True if character is lowercase
- `sum()` with generator expression efficiently counts matching characters
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

---

## Problem 4: Extract Even Numbers from List

**Problem Statement:**
Write a Python program to print the even numbers from a given list.

**Input:** `[1, 2, 3, 4, 5, 6, 7, 8, 9]`  
**Output:** `[2, 4, 6, 8]`

### Solution (Method 1: List Comprehension)

```python
def get_even_numbers(lst):
    """Returns even numbers using list comprehension."""
    return [num for num in lst if num % 2 == 0]

# Test
sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(get_even_numbers(sample_list))  # [2, 4, 6, 8]
```

### Solution (Method 2: Using filter())

```python
def get_even_numbers_v2(lst):
    """Returns even numbers using filter()."""
    return list(filter(lambda x: x % 2 == 0, lst))

# Test
print(get_even_numbers_v2(sample_list))  # [2, 4, 6, 8]
```

**Explanation:**
- `num % 2 == 0` - Modulo operator checks if number is divisible by 2 (even)
- List comprehension is more Pythonic and readable
- `filter()` with lambda is functional programming approach
- **Time Complexity:** O(n)
- **Space Complexity:** O(m) where m is count of even numbers

---

## Problem 5: Check if Number is Perfect

**Problem Statement:**
Write a Python function to check whether a number is perfect or not.

A Perfect number is a number that is half the sum of all of its positive divisors (including itself).

**Examples:** 6, 28, 496, 8128

### Solution

```python
def is_perfect_number(n):
    """Checks if a number is perfect."""
    if n <= 0:
        return False
    # Sum of all proper divisors (excluding n itself)
    divisor_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisor_sum == n

# Test
test_numbers = [6, 28, 496, 8128, 10, 15, 20]
for num in test_numbers:
    print(f"{num}: {is_perfect_number(num)}")
```

**Explanation:**
- A perfect number equals the sum of its proper divisors
 sum = 1+2+3 =  Perfect!6 
 sum = 1+2+4+7+14 =  Perfect!28 
 sum = 1+2+5 =  Not perfect8 
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

---

## Problem 6: Concatenate Multiple Dictionaries

**Problem Statement:**
Write a Python function to concatenate any number of dictionaries to create a new one.

**Input:**
```python
dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}
```
**Output:** `{1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}`

### Solution (Method 1: Using update())

```python
def merge_dictionaries(*dicts):
    """Merges multiple dictionaries using update()."""
    result = {}
    for d in dicts:
        result.update(d)
    return result

# Test
dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}
merged = merge_dictionaries(dic1, dic2, dic3)
print(merged)  # {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
```

### Solution (Method 2: Dictionary Comprehension - Python 3.5+)

```python
def merge_dictionaries_v2(*dicts):
    """Merges using dictionary comprehension and unpacking."""
    return {k: v for d in dicts for k, v in d.items()}

print(merge_dictionaries_v2(dic1, dic2, dic3))
```

### Solution (Method 3: Using ** unpacking - Python 3.9+)

```python
def merge_dictionaries_v3(*dicts):
    """Merges using ** unpacking."""
    result = {}
    for d in dicts:
        result |= d  # Merge operator
    return result
```

**Explanation:**
- `*dicts` - Accepts variable number of dictionary arguments
- `update()` - Adds all key-value pairs from one dict to another
- Dictionary comprehension iterates through all dicts and their items
- **Time Complexity:** O(n) where n is total items
- **Space Complexity:** O(n)

---

## Problem 7: Find Most Frequent Word

**Problem Statement:**
Write a python function that accepts a string as input and returns the word with most occurrence.

**Input:** `hello how are you i am fine thank you`  
**Output:** `you -> 2`

### Solution

```python
def most_frequent_word(string):
    """Returns the most frequently occurring word(s)."""
    from collections import Counter
    words = string.split()
    word_counts = Counter(words)
    max_count = max(word_counts.values())
    most_freq = [word for word, count in word_counts.items() if count == max_count]
    return most_freq, max_count

# Test
sample_input = "hello how are you i am fine thank you"
words_list, count = most_frequent_word(sample_input)
for word in words_list:
    print(f"{word} -> {count}")
```

**Explanation:**
- `Counter` from collections module counts word occurrences
- `max(word_counts.values())` finds the maximum count
- List comprehension filters words with maximum count
- Handles ties (multiple words with same max count)
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

---

## Problem 8: Create Histogram with Bin Size 10

**Problem Statement:**
Write a python function that receives a list of integers and prints out a histogram of bin size 10.

**Input:** `[13,42,15,37,22,39,41,50]`  
**Output:** `{'11-19': 2, '21-29': 1, '31-39': 2, '41-49': 2, '51-59': 1}`

### Solution

```python
def create_histogram(numbers, bin_size=10):
    """Creates a histogram with specified bin size."""
    histogram = {}
    for num in numbers:
        bin_start = (num // bin_size) * bin_size
        bin_end = bin_start + (bin_size - 1)
        bin_key = f"{bin_start+1}-{bin_end}"
        
        if bin_key not in histogram:
            histogram[bin_key] = 0
        histogram[bin_key] += 1
    
    return dict(sorted(histogram.items()))

# Test
sample_input = [13, 42, 15, 37, 22, 39, 41, 50]
histogram = create_histogram(sample_input)
print(histogram)
```

**Explanation:**
- `bin_start = (num // bin_size) * bin_size` - Calculates bin start
  - For 13: (13//10)*10 = 1*10 = 10
  - Bin range: 11-19
- For each number, increment its bin count
- `sorted()` sorts bins numerically
- **Time Complexity:** O(n log k) where k is number of bins
- **Space Complexity:** O(k)

---

## Problem 9: Find Nearest Coordinate

**Problem Statement:**
Write a python function that accepts a list of 2D co-ordinates and a query point, and then finds the co-ordinate which is closest in terms of distance from the query point.

**Input:**
```
Coordinates: [(1,1),(2,2),(3,3),(4,4)]
Query Point: (0,0)
```
**Output:** `Nearest to (0,0) is (1,1)`

### Solution

```python
def find_nearest_coordinate(coordinates, query_point):
    """Finds the nearest coordinate using Euclidean distance."""
    import math
    
    min_distance = float('inf')
    nearest_point = None
    
    for coord in coordinates:
        # Euclidean distance formula: sqrt((x2-x1)^2 + (y2-y1)^2)
        distance = math.sqrt((coord[0] - query_point[0])**2 + 
                            (coord[1] - query_point[1])**2)
        if distance < min_distance:
            min_distance = distance
            nearest_point = coord
    
    return nearest_point, min_distance

# Test
coordinates = [(1,1), (2,2), (3,3), (4,4)]
query_point = (0, 0)
nearest, distance = find_nearest_coordinate(coordinates, query_point)
print(f"Nearest to {query_point} is {nearest} (distance: {distance:.2f})")
```

**Explanation:**
]]  + (-)yy- **[(-)xxDistance:** 
- For (1,1)  1.412 1-]] = 0)0)0): 
- For (2,2)  2.838 2-]] = 0)0)0): 
- (1,1) is nearest with distance 1.41
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

---

## Problem 10: Bag of Words

**Problem Statement:**
Write a python function that receives a list of strings and performs bag of word operation on those strings.

Bag of Words treats text as unordered collection of words, counting word frequencies.

### Solution

```python
def bag_of_words(strings):
    """Creates a bag of words model from a list of strings."""
    from collections import Counter
    all_words = []
    
    for string in strings:
        words = string.lower().split()
        all_words.extend(words)
    
    word_freq = Counter(all_words)
    return word_freq

# Test
sample_strings = [
    "the cat sat on the mat",
    "the dog sat on the log",
    "cats and dogs are friends"
]
bow = bag_of_words(sample_strings)
print(dict(bow))
```

**Output:**
```python
{'the': 4, 'cat': 1, 'sat': 2, 'on': 2, 'mat': 1, 'dog': 1, 'log': 1, 'cats': 1, 'and': 1, 'dogs': 1, 'are': 1, 'friends': 1}
```

**Explanation:**
- Bag of Words is NLP technique that ignores word order and grammar
- Counts frequency of each word across all documents
- Useful for text classification, sentiment analysis, etc.
- Convert to lowercase for case-insensitive counting
- **Time Complexity:** O(n*m) where n is strings, m is avg length
- **Space Complexity:** O(k) where k is unique words

---

## Problem 11: Add Three Lists using map() and lambda

**Problem Statement:**
Write a Python program to add three given lists using Python map and lambda.

### Solution

```python
def add_three_lists(list1, list2, list3):
    """Adds corresponding elements from three lists."""
    return list(map(lambda x, y, z: x + y + z, list1, list2, list3))

# Test
list1 = [1, 2, 3, 4, 5]
list2 = [2, 3, 4, 5, 6]
list3 = [3, 4, 5, 6, 7]
result = add_three_lists(list1, list2, list3)
print(result)  # [6, 9, 12, 15, 18]
```

**Explanation:**
- `map()` applies function to corresponding elements from all lists
- Automatically stops at shortest list
- `lambda x, y, z: x + y + z` takes 3 arguments and adds them
- Returns iterator, convert to list for display
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

---

## Problem 12: Power List using map()

**Problem Statement:**
Write a Python program to create a list containing the power of said number in bases raised to the corresponding number in the index using Python map.

**Input:** `[1,2,3,4,5,6]`  
**Output:** `[1, 2, 9, 64, 625, 7776]`

### Solution

```python
def power_list(numbers):
    """Raises each number to the power of its index position."""
    return list(map(lambda x: x[1] ** x[0], enumerate(numbers)))

# Test
list_input = [1, 2, 3, 4, 5, 6]
result = power_list(list_input)
print(result)  # [1, 2, 9, 64, 625, 7776]

# Explanation of results:
# 1^0 = 1
# 2^1 = 2
# 3^2 = 9
# 4^3 = 64
# 5^4 = 625
# 6^5 = 7776
```

**Explanation:**
- `enumerate()` returns (index, value) tuples
- `x[0]` is the index, `x[1]` is the value
- `lambda x: x[1] ** x[0]` raises value to power of index
- `**` is the exponentiation operator
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

---

## Problem 13: Filter Vowels using filter()

**Problem Statement:**
Using filter() and list() functions and .lower() method filter all the vowels in a given string.

### Solution

```python
def filter_vowels(string):
    """Removes all vowels from a string."""
    vowels = 'aeiou'
    return ''.join(filter(lambda x: x.lower() not in vowels, string))

# Test
sample_string = "Hello World! This is Amazing."
result = filter_vowels(sample_string)
print(result)  # Hll Wrld! Ths s mzng.
```

**Explanation:**
- `filter()` selects elements where condition is True
- `lambda x: x.lower() not in vowels` - Keep char if it's NOT a vowel
- `x.lower()` converts to lowercase for case-insensitive comparison
- `''.join()` combines filtered characters back into string
- Non-alphabetic characters (spaces, punctuation) are kept
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

---

## Problem 14: Convert 2D List to 1D using reduce()

**Problem Statement:**
Use reduce to convert a 2D list to 1D.

### Solution

```python
from functools import reduce

def flatten_2d_list(list_2d):
    """Converts 2D list to 1D using reduce()."""
    return reduce(lambda x, y: x + y, list_2d)

# Test
list_2d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = flatten_2d_list(list_2d)
print(result)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

**Alternative using list comprehension:**

```python
def flatten_2d_list_v2(list_2d):
    """Using list comprehension."""
    return [item for sublist in list_2d for item in sublist]
```

**Explanation:**
- `reduce()` applies function cumulatively to items (from left to right)
- `lambda x, y: x + y` concatenates two lists
- First iteration: [1,2,3] + [4,5,6] = [1,2,3,4,5,6]
- Second iteration: [1,2,3,4,5,6] + [7,8,9] = [1,2,3,4,5,6,7,8,9]
- List comprehension is more Pythonic
- **Time Complexity:** O(n*m) where n is sublists, m is avg size
- **Space Complexity:** O(n*m)

---

## Problem 15: Filter Highly Skilled Employees

**Problem Statement:**
A dictionary contains information about 5 employees with fields: First name, Last name, Age, Grade (Skilled, Semi-skilled, Highly skilled).

Write a program using map/filter/reduce to return a list of employees (first name + last name) who are highly skilled.

### Solution

```python
employees = [
    {'fname':'Nitish', 'lname':'Singh', 'age': 33, 'grade':'skilled'},
    {'fname':'Ankit', 'lname':'Verma', 'age': 34, 'grade':'semi-skilled'},
    {'fname':'Neha', 'lname':'Singh', 'age': 35, 'grade':'highly-skilled'},
    {'fname':'Anurag', 'lname':'Kumar', 'age': 30, 'grade':'skilled'},
    {'fname':'Abhinav', 'lname':'Sharma', 'age': 37, 'grade':'highly-skilled'}
]

def get_highly_skilled_employees(emp_list):
    """Returns full names of highly-skilled employees."""
    return list(map(
        lambda x: x['fname'] + ' ' + x['lname'],
        filter(lambda x: x['grade'] == 'highly-skilled', emp_list)
    ))

# Test
result = get_highly_skilled_employees(employees)
print(result)  # ['Neha Singh', 'Abhinav Sharma']
```

**Explanation:**
- **Step 1 - filter():** `filter(lambda x: x['grade'] == 'highly-skilled', emp_list)`
  - Selects only employees with grade = 'highly-skilled'
  - Result: [Neha dict, Abhinav dict]

- **Step 2 - map():** `map(lambda x: x['fname'] + ' ' + x['lname'], filtered_list)`
  - Transforms each employee dict to full name string
  - Concatenates first and last names
  - Result: ['Neha Singh', 'Abhinav Sharma']

 Result
- **Time Complexity:** O(n)
- **Space Complexity:** O(m) where m is highly-skilled employees

---

## Summary of Key Concepts

### Functional Programming
- **map()** - Transform each element
- **filter()** - Select elements matching condition
- **reduce()** - Accumulate to single value
- **lambda** - Anonymous functions for concise operations

### Alternative Approaches
- List comprehensions instead of map/filter (more Pythonic)
- Generator expressions for memory efficiency
- Built-in functions like `Counter`, `sorted()`, `sum()`

### Time & Space Complexity
| Problem | Time | Space | Notes |
|---------|------|-------|-------|
| 1. Unique | O(n) | O(n) | Set creation |
| 2. Sort | O(n log n) | O(n) | Sorting words |
| 3. Case Count | O(n) | O(1) | Single pass |
| 4. Even Numbers | O(n) | O(k) | k = even count |
| 5. Perfect Number | O(n) | O(1) | Divisor search |
| 6. Merge Dict | O(n) | O(n) | All items |
| 7. Frequent Word | O(n) | O(n) | Counter needed |
| 8. Histogram | O(n) | O(k) | k = bins |
| 9. Nearest Coord | O(n) | O(1) | Distance calc |
| 10. Bag of Words | O(n*m) | O(k) | k = unique words |
| 11. Add Lists | O(n) | O(n) | New list |
| 12. Power List | O(n) | O(n) | Exponentiation |
| 13. Filter Vowels | O(n) | O(n) | New string |
| 14. Flatten 2D | O(n*m) | O(n*m) | All elements |
| 15. Filter Emp | O(n) | O(m) | m = filtered |

