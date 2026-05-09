"""1. What are Python’s key features?  
2. Difference between list, tuple, and set  
3. What is PEP8? Why is it important?  
4. What are Python data types?  
5. Mutable vs Immutable objects  
6. What is list comprehension?  
7. Difference between is and ==  
8. What are Python decorators?  
9. Explain *args and **kwargs  
10. What is a lambda function?  
11. Difference between deep copy and shallow copy  
12. How does Python memory management work?  
13. What is a generator?  
14. Difference between iterable and iterator  
15. How does with statement work?  
16. What is a context manager?  
17. What is _init_.py used for?  
18. Explain Python modules and packages  
19. What is _name_ == "_main_"?  
20. What are Python namespaces?  
21. Explain Python’s GIL (Global Interpreter Lock)  
22. Multithreading vs multiprocessing in Python  
23. What are Python exceptions?  
24. Difference between try-except and assert  
25. How to handle file operations?  
26. What is the difference between @staticmethod and @classmethod?  
27. How to implement a stack or queue in Python?  
28. What is duck typing in Python?  
29. Explain method overloading and overriding
30. What is the difference between Python 2 and Python 3?  
31. What are Python’s built-in data structures?  
32. Explain the difference between sort() and sorted()  
33. What is a Python dictionary and how does it work?  
34. What are sets and frozensets?  
35. Use of enumerate() function  
36. What are Python itertools?  
37. What is a Python virtual environment?  
38. How do you install packages in Python?  
39. What is pip?  
40. How to connect Python to a database?  
41. Explain regular expressions in Python  
42. How does Python handle memory leaks?  
43. What are Python’s built-in functions?  
44. Use of map(), filter(), reduce()  
45. How to handle JSON in Python?  
46. What are data classes?  
47. What are f-strings and how are they useful?  
48. Difference between global, nonlocal, and local variables  
49. Explain unit testing in Python  
50. How would you debug a Python application"""

# Defining sets in Python

def add_matrix(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
C = add_matrix(A, B)
print(C)

def subtract_matrix(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
C = subtract_matrix(A, B)
print(C)

def split_matrix(A):
    mid = len(A) // 2
    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]
    return A11, A12, A21, A22
A = [[1, 2], [3, 4]]
# B = [[5, 6], [7, 8]]
C = split_matrix(A)
print(C)

def strassen(A, B):
    n = len(A)
    # Base case: 1x1 matrix
    if n == 1:
        return [[A[0][0] * B[0][0]]]

    # Split matrices into quadrants
    A11, A12, A21, A22 = split_matrix(A)
    B11, B12, B21, B22 = split_matrix(B)

    # Calculating the 7 products (P1 to P7)
    P1 = strassen(A11, subtract_matrix(B12, B22))
    P2 = strassen(add_matrix(A11, A12), B22)
    P3 = strassen(add_matrix(A21, A22), B11)
    P4 = strassen(A22, subtract_matrix(B21, B11))
    P5 = strassen(add_matrix(A11, A22), add_matrix(B11, B22))
    P6 = strassen(subtract_matrix(A12, A22), add_matrix(B21, B22))
    P7 = strassen(subtract_matrix(A11, A21), add_matrix(B11, B12))

    # Calculating the 4 quadrants of the result
    C11 = add_matrix(subtract_matrix(add_matrix(P5, P4), P2), P6)
    C12 = add_matrix(P1, P2)
    C21 = add_matrix(P3, P4)
    C22 = subtract_matrix(subtract_matrix(add_matrix(P5, P1), P3), P7)

    # Combine quadrants into a single matrix
    C = []
    for i in range(len(C11)):
        C.append(C11[i] + C12[i])
    for i in range(len(C21)):
        C.append(C21[i] + C22[i])
        
    return C
# A = [[1, 2], [3, 4]]
# B = [[5, 6], [7, 8]]
# C = strassen(A)
# print(C)

# # Example usage:
# A = [[1, 2], [3, 4]]
# B = [[5, 6], [7, 8]]
# C = strassen(A, B)