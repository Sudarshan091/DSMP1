class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overloading the print/string behavior
    def __str__(self):
        return f"Point({self.x}, {self.y})"

    # Overloading the '+' operator
    def __add__(self, other):
        # self represents the first object (p1)
        # other represents the second object (p2)
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Point(new_x, new_y)

# Creating two Point objects
p1 = Point(2, 4)
p2 = Point(5, 1)

# Using the overloaded '+' operator
p3 = p1 + p2

print(p3)  # Output: Point(7, 5)