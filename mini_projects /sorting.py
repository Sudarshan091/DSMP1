"""Step 1: Initialize two variables, largest and second_largest, to negative infinity.

Step 2: Loop through each number in the array exactly once.

Step 3: If the current number is strictly greater than largest:

Update second_largest to hold the previous value of largest.

Update largest to be the current number.

Step 4: If the current number is strictly less than largest but greater than second_largest:

Update second_largest to be the current number.

Step 5: Return second_largest."""


def get_second_largest(arr):
    # Step 1: Initialize largest and second_largest to negative infinity.
    # In Python, float('-inf') represents negative infinity.
    largest = float('-inf')
    second_largest = float('-inf')
    
    # Step 2: Loop through each number in the array exactly once.
    for num in arr:
        
        # Step 3: If the current number is strictly greater than largest
        if num > largest:
            # The current largest is being replaced, so it becomes the second largest
            second_largest = largest
            # The current number is now the new largest
            largest = num
            
        # Step 4: If current number is strictly less than largest, 
        # BUT greater than second_largest
        elif num < largest and num > second_largest:
            # Update second_largest to be the current number
            second_largest = num
            
    # Step 5: Return the final result
    return second_largest

# Test the function to see if your logic works
my_list = [10, 10, 8, 5]
print(get_second_largest(my_list))

